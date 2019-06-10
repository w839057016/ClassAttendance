
import face_recognition
import cv2
import os
import pymysql
import time


def comparison(teacher_id):
    current = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #print(current)
    known_filelist = []
    unknown_path = "unknown_dispose_face/"
    known_path = "known_dispose_face/"
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="19951208",
                         db="face_recognition",
                         port=3306,
                         charset='utf8')
    cursor = db.cursor()
    sql = "SELECT course_stu_id,course_id FROM course WHERE course_teacher_id='%s'" % teacher_id
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            known_filelist.append(row[0])
            course_id = row[1]
            #print(known_filelist)
    except:
        print("Error : unable to fetch data")
    unknown_fileList = os.listdir(unknown_path)
    #print(unknown_path + unknown_file)
    count = True
    for known_file in known_filelist:
        print(known_path + known_file + ".jpg")
        known_image = face_recognition.load_image_file(known_path + known_file + ".jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]
        if count:
            for unknown_file in unknown_fileList:
                print(unknown_file)
                unknown_image = face_recognition.load_image_file(unknown_path + unknown_file)
                try:
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.45)
                    if results[0]:
                        print(known_file)
                        break
                except:
                    count = False
                    print("")
        if count==False:
            unknown_image = face_recognition.load_image_file("unknown_face/1.jpg")
            unknown_encodings = face_recognition.face_encodings(unknown_image)
            for unknown_encoding in unknown_encodings:
                results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.45)
                if results[0]:
                    print(known_file)
                    break


        print(results[0])
        if results[0]:
            check_result = "到课"
        else:
            check_result = "缺勤"
        sql = "INSERT INTO face_recognition.check VALUE('%s','%s','%s','%s')" % (
        known_file, course_id, current, check_result)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print("插入成功")
        except:
            db.rollback()
            print("error")
    db.close()
    os.remove("unknown_face/1.jpg")

    #for unknown_file in unknown_fileList:
        #os.remove( unknown_path+unknown_file)

