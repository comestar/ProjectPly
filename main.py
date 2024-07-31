from src import *
# label = 9
#
# file = 'E:/Cloud/realpoint2/side4.ply'
# destfile = 'data/side4.ply'
#
# plydata = get_plydata_ply_xyz(file)
#
# plydata = serialization_to_ply(plydata)
#
# plydata = set_label(plydata, label)
#
# plydata.write(destfile)
file0 = 'data/des.ply'
file1 = 'data/side4.ply'
# fuse_ply_des(file0, file1)
extract_label_dest(file0,0)