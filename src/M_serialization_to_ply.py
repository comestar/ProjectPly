import numpy as np

from plyfile import PlyData, PlyElement
# not source.dtype == [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('label', 'f4'), ('pixel_x', 'f4'),
#                             ('pixel_y', 'f4')]
def serialization_to_ply(source: np.ndarray):
    if not source.dtype == [('x', 'i4'), ('y', 'i4'), ('z', 'i4'), ('label', 'f4'), ('pixel_x', 'f4'),
                            ('pixel_y', 'f4')] :
        #对于不完整的ply进行填充
        if len(source[0]) == 3:
            sidearray = [(np.nan, np.nan, np.nan)] * len(source)
            source = np.hstack((source, sidearray))
        source = [tuple(row) for row in source]
        source = np.array(source, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('label', 'f4'), ('pixel_x', 'f4'),
                                         ('pixel_y', 'f4')])
    source = source.ravel()
    element = PlyElement.describe(source, 'vertex')
    # 这里函数希望获得一个PlyProperity对象，不过函数也有自适应机制，输入数组即可
    plydata = PlyData([element], text=True)
    return plydata
