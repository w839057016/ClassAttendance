import dlib         # 人脸识别的库dlib
import numpy as np  # 数据处理的库numpy
import cv2          # 图像处理的库OpenCv



def face_cutting(path_read,file_name,path_save):
    # dlib预测器
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')
    # 读取图像的路径
    #path_read = "face/"
    img = cv2.imread(path_read + file_name)
    # 用来存储生成的单张人脸的路径
    #path_save = "face/"
    # dlib检测
    dets = detector(img, 1)
    print("人脸数：", len(dets))
    for k, d in enumerate(dets):
        # 计算矩形大小
        # (x,y), (宽度width, 高度height)
        pos_start = tuple([d.left(), d.top()])
        pos_end = tuple([d.right(), d.bottom()])
        # 计算矩形框大小
        height = d.bottom() - d.top()
        width = d.right() - d.left()

        # 根据人脸大小生成空的图像
        img_blank = np.zeros((height, width, 3), np.uint8)

        for i in range(height):
            for j in range(width):
                img_blank[i][j] = img[d.top() + i][d.left() + j]

        #cv2.imshow("face_" + str(k + 1), img_blank)显示图片
        cv2.imwrite(path_save + file_name, img_blank)
        break;
    cv2.waitKey(0)