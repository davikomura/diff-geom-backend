import numpy as np

def compute_second_fundamental_form(x, y, z, u, v, normals):
    du = u[0,1] - u[0,0]
    dv = v[1,0] - v[0,0]
    
    x_u, x_v = np.gradient(x, dv, du, edge_order=2)
    y_u, y_v = np.gradient(y, dv, du, edge_order=2)
    z_u, z_v = np.gradient(z, dv, du, edge_order=2)

    x_uu, x_uv = np.gradient(x_u, dv, du, edge_order=2)
    y_uu, y_uv = np.gradient(y_u, dv, du, edge_order=2)
    z_uu, z_uv = np.gradient(z_u, dv, du, edge_order=2)

    _, x_vv = np.gradient(x_v, dv, du, edge_order=2)
    _, y_vv = np.gradient(y_v, dv, du, edge_order=2)
    _, z_vv = np.gradient(z_v, dv, du, edge_order=2)

    Xuu = np.stack((x_uu, y_uu, z_uu), axis=-1)
    Xuv = np.stack((x_uv, y_uv, z_uv), axis=-1)
    Xvv = np.stack((x_vv, y_vv, z_vv), axis=-1)

    L = np.einsum('ijk,ijk->ij', normals, Xuu)
    M = np.einsum('ijk,ijk->ij', normals, Xuv)
    N = np.einsum('ijk,ijk->ij', normals, Xvv)

    return L, M, N
