from src import *
import os

#函数目的在于将一个目录下的点云文件按序给与标签，而后融合
# 1.读取文件
# 2.设置标签
# 3.融合
def fuse_contents(file=r'../data'):
    filename = os.listdir(file)
    for i, label in zip(filename, range(len(filename))):
        plydata = get_plydata_ply_xyz(file + '/' + i)
        plydata = serialization_to_ply(plydata)
        plydata = set_label(plydata, label)
        if label == 0:
            des_plydata = plydata
        else:
            des_plydata['vertex'].data = np.hstack((des_plydata['vertex'].data, plydata['vertex'].data))  #融合
    des_plydata.write('fusion.ply')


fuse_contents('../data')
