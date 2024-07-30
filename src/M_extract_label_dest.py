from src import *
def extract_label_dest(file , ilabel : int):
    plydata = PlyData.read(file)
    ser_source = np.array([i for i, label in zip(plydata['vertex'].data, plydata['vertex']['label']) if label == ilabel])
    extract_plydata = serialization_to_ply(ser_source)
    return extract_plydata

