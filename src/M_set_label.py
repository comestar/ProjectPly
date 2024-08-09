from plyfile import PlyData


def set_label(plydata: PlyData, label: int):
    plydata['vertex']['label'] = label
    return plydata
