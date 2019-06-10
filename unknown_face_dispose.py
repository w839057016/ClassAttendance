import os
import unknown_face_cutting
from PIL import Image


def dispose():
    filepath = "unknown_face/"
    file_save_path = "unknown_dispose_face/"
    filelist = os.listdir(filepath)
    # os.remove(filepath+"1.jpg")
    for filename in filelist:
        print(filename)
        unknown_face_cutting.face_cutting(filepath, filename, file_save_path)

    fileList = os.listdir(file_save_path)
    for name in fileList:
        print(name)
        im = Image.open(file_save_path + name)
        (x, y) = im.size
        print(im.size)
        out = im.resize((150, 150), Image.ANTIALIAS).save(file_save_path + name)


