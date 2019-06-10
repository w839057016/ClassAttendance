import pymysql
import pymysql.cursors
connection=pymysql.connect(host="localhost",
                           user="root",
                           password="19951208",
                           db="face_recognition",
                           port=3306,
                           charset='utf8'
                           )
cursor=connection.cursor()
cursor.execute("SELECT VERSION()")
row=cursor.fetchone()
print("mysql server version",row[0])
cursor.close()