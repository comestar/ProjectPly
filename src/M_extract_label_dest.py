import numpy as np

from plyfile import PlyData, PlyElement

from .M_serialization_to_ply import serialization_to_ply


def extract_label_dest(file, ilabel: int, desfile = 'data/dest.ply'):
    plydata = PlyData.read(file)
    ser_source = np.array(
        [i for i, label in zip(plydata['vertex'].data, plydata['vertex']['label']) if label == ilabel])
    print(ser_source)

    plydata = serialization_to_ply(ser_source)
    plydata.write(desfile)
    return plydata
