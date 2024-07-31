import numpy as np

from plyfile import PlyData

from .M_serialization_to_ply import serialization_to_ply

def get_plydata_ply_xyz(sourfile: str) -> np.ndarray:
    plydata = PlyData.read(sourfile)
    vertex = plydata['vertex']
    plydata = np.array((vertex['x'], vertex['y'], vertex['z'])).T
    return plydata
