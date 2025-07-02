import numpy as np

def compute_normals(Xu, Xv):

    normal = np.cross(Xu, Xv, axis=-1)
    norm = np.linalg.norm(normal, axis=-1, keepdims=True)
    N = normal / norm
    return N
