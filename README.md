# README

描述：这是我 2018 年在校期间，在老师的指导下，参考网上的文档，使用 Python 开发的一个小项目，使用人脸识别技术方便教师考勤点到。

使用到的技术：

- Web 前端：Bootstrap 3.3.7
- Web 后端：flask, flask-sqlalchemy
- 人脸识别相关：dlib, numpy, cv2, [face_recognition](https://github.com/ageitgey/face_recognition)
- 微信 API

使用方法：

1. 先在后台登记学生信息，上传学生照片进行训练
2. 教师课堂拍照，并把照片上传到微信公众号
3. 后台进行人脸识别，并将结果发给教师微信号
