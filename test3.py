import face_recognition
unknown_image=face_recognition.load_image_file("unknown_dispose_face/2_1.jpg")
unknown_encoding=face_recognition.face_encodings(unknown_image)[0]
known_image=face_recognition.load_image_file("known_dispose_face/2018122911.jpg")
known_encoding=face_recognition.face_encodings(known_image)[0]
results=face_recognition.compare_faces([known_encoding],unknown_encoding,tolerance=0.4)
print(results[0])