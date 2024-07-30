from src import *
def get_plydata_ply_xyz(sourfile: str) -> np.ndarray:
    plydata = PlyData.read(sourfile)
    vertex = plydata['vertex']
    source = np.array((vertex['x'], vertex['y'], vertex['z'])).T
    plydata = serialization_to_ply(source)
    return plydata
