import numpy as np

def compute_partials(x, y, z, u, v):
    du = u[0,1] - u[0,0]
    dv = v[1,0] - v[0,0]
    
    x_v, x_u = np.gradient(x, dv, du, edge_order=2)
    y_v, y_u = np.gradient(y, dv, du, edge_order=2)
    z_v, z_u = np.gradient(z, dv, du, edge_order=2)

    Xu = np.stack((x_u, y_u, z_u), axis=-1)
    Xv = np.stack((x_v, y_v, z_v), axis=-1)

    return Xu, Xv
