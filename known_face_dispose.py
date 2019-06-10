from PIL import Image
import os
import known_face_cutting
filepath="known_face/"
filelist=os.listdir(filepath)

for filename in filelist:
    print(filename)
    known_face_cutting.face_cutting(filepath,filename,"known_face/")
    im = Image.open("known_face/" + filename)
    (x, y) = im.size
    print(im.size)
    out = im.resize((150,150), Image.ANTIALIAS).save("known_dispose_face/" + filename)




