from flask import Flask, render_template,request,redirect,url_for,session,flash
import config
from models import User
from exts import db
import pymysql


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/index/')
def index():
    message="首页"
    return  render_template('index.html',message=message)
@app.route('/',methods=['GET','POST'])
def login():
    message="提示信息："
    if request.method=='GET':
        return render_template('login.html')
    else:
        username=request.form.get('user')
        password=request.form.get('password')
        user=User.query.filter(User.id==username,User.password==password).first()
        if user:
            session['user_id']=user.id
            session.permanent=True
            return redirect(url_for('index'))
        else:
            message=message+"用户名或密码输入错误，请重试！"
            return render_template('login.html',massage=message)
@app.route('/select_teacher/')
def select_teacher():
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="19951208",
                             db="face_recognition",
                             port=3306,
                             charset='utf8')
        cursor = db.cursor()
        sql = "SELECT * FROM teacher"
        cursor.execute(sql)
        u=cursor.fetchall()
        db.close()
        return render_template('select_teacher.html',u=u)
@app.route('/insert_teacher/',methods=['GET','POST'])
def insert_teacher():
    message="提示信息："
    if request.method=='GET':
        return render_template('insert_teacher.html',message=message)
    else:
        teacher_name=request.form.get('teacher_name')
        teacher_id=request.form.get('teacher_id')
        teacher_sex=request.form.get('teacher_sex')
        teacher_wx=request.form.get('teacher_wx')
        print(type(teacher_name))
        print(type(teacher_id))
        print(type(teacher_sex))
        print(type(teacher_wx))
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="19951208",
                             db="face_recognition",
                             port=3306,
                             charset='utf8')
        cursor=db.cursor()
        sql="SELECT t_id FROM teacher"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            print(i[0])
            if i[0]==teacher_id:
                message=message+"该工号教师已存在请重新插入"
                return render_template('insert_teacher.html',message=message)
        sql="INSERT INTO teacher(t_name,t_id,t_sex,t_wx) VALUES ('%s','%s','%s','%s')" % (teacher_name,teacher_id,teacher_sex,teacher_wx)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            print("error")
        db.close()
        message="数据插入成功！"
        return render_template('index.html',message=message)
@app.route("/alter_teacher/",methods=["GET","POST"])
def alter_teacher():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="19951208",
                         db="face_recognition",
                         port=3306,
                         charset='utf8')
    cursor = db.cursor()
    sql="SELECT t_id FROM teacher"
    cursor.execute(sql)
    t=cursor.fetchall()

    if request.method=="GET":
        return render_template("alter_teacher.html",t=t)
    else:
        teacher_id=request.form.get('teacher_id')
        alter_information=request.form.get('alter_information')
        information=request.form.get('information')
        if alter_information=="教师姓名":
            sql="UPDATE teacher SET t_name='%s' WHERE t_id='%s'" % (information,teacher_id)
        elif alter_information=="教师微信id":
            sql="UPDATE teacher SET t_wx='%s' WHERE t_id='%s'" % (information,teacher_id)
        elif alter_information == "教师性别":
            sql = "UPDATE teacher SET t_sex='%s' WHERE t_id='%s'" % (information, teacher_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('error')
            db.rollback()
        db.close()
        message="修改教师信息成功"
        return render_template("index.html",message=message)
@app.route('/delete_teacher/',methods=['GET','POST'])
def delete_teacher():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="19951208",
                         db="face_recognition",
                         port=3306,
                         charset='utf8')
    cursor = db.cursor()
    sql = "SELECT t_id FROM teacher"
    cursor.execute(sql)
    t = cursor.fetchall()
    if request.method=="GET":
        return render_template("delete_teacher.html",t=t)
    else:
        teacher_id = request.form.get('teacher_id')
        print(teacher_id)
        sql="DELETE FROM teacher WHERE t_id='%s'" % teacher_id
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('error')
            db.rollback()
        db.close()
        message="删除教师数据成功"
        return render_template("index.html",message=message)
if __name__ == '__main__':
    app.run()
