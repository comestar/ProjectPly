import cv2

from src import *
label = 11

# file = 'E:/Cloud/realpoint2/under.ply'
# destfile = 'data/under.ply'
#
# plydata = get_plydata_ply_xyz(file)
#
# plydata = serialization_to_ply(plydata)
#
# plydata = set_label(plydata, label)
#
# plydata.write(destfile)

# file0 = 'data/des.ply'
# file1 = 'data/under.ply'
# fuse_ply_des(file0, file1)


# extract_label_dest(file0,0)


# a = 'asdfsdf'
# print(list(a))

# file = "C:/Users/Yu-hf/Pictures/Screenshots/a.png"
# img = cv2.imread(file)
# img = cv2.resize(img,(338,255))
# cv2.imwrite(file,img)

import os

file = os.listdir(r'data')

print(file)
