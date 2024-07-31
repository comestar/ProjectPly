from src import *
file = 'E:/Cloud/realpoint2/0.ply'
plydata = get_plydata_ply_xyz(file)
print(hasattr(plydata, 'dtype'))
print(plydata.dtype)
plydata = serialization_to_ply(plydata)

# plydata = set_label(plydata, 0)
# plydata.write('E:/Cloud/realpoint2/0.ply')