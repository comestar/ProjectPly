import numpy as np

from plyfile import PlyData, PlyElement

def serialization_to_ply(source: np.ndarray, destfile='data/dest.ply'):
    if not source.dtype == [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('label', 'f4'), ('pixel_x', 'f4'),
                            ('pixel_y', 'f4')]:
        sidearray = [(np.nan, np.nan, np.nan)] * len(source)
        source = np.hstack((source, sidearray))
        source = [tuple(row) for row in source]
        source = np.array(source, dtype=[('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('label', 'f4'), ('pixel_x', 'f4'),
                                         ('pixel_y', 'f4')])
    element = PlyElement.describe(source, 'vertex')
    # 这里函数希望获得一个PlyProperity对象，不过函数也有自适应机制，输入数组即可
    plydata = PlyData([element], text=True)
    plydata.write(destfile)
    return plydata
