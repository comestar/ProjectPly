import numpy as np

from plyfile import PlyData

def fuse_ply_des(file0, file1, desfile='data/des.ply'):
    plydata1 = PlyData.read(file1)
    plydata0 = PlyData.read(file0)
    plydata1['vertex'].data = np.hstack((plydata1['vertex'].data, plydata0['vertex'].data))
    print(plydata1['vertex'].data)
    plydata1.write(desfile)
