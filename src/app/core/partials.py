import numpy as np

def compute_partials(x, y, z, u, v):
    du = u[0,1] - u[0,0]
    dv = v[1,0] - v[0,0]
    
    x_u, x_v = np.gradient(x, dv, du, edge_order=2)
    y_u, y_v = np.gradient(y, dv, du, edge_order=2)
    z_u, z_v = np.gradient(z, dv, du, edge_order=2)

    Xu = np.stack((x_u, y_u, z_u), axis=-1)
    Xv = np.stack((x_v, y_v, z_v), axis=-1)

    return Xu, Xv
