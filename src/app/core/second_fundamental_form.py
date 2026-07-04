import numpy as np

def compute_second_fundamental_form(x, y, z, u, v, normals):
    du = u[0,1] - u[0,0]
    dv = v[1,0] - v[0,0]
    
    x_v, x_u = np.gradient(x, dv, du, edge_order=2)
    y_v, y_u = np.gradient(y, dv, du, edge_order=2)
    z_v, z_u = np.gradient(z, dv, du, edge_order=2)

    x_uv, x_uu = np.gradient(x_u, dv, du, edge_order=2)
    y_uv, y_uu = np.gradient(y_u, dv, du, edge_order=2)
    z_uv, z_uu = np.gradient(z_u, dv, du, edge_order=2)

    x_vv, _ = np.gradient(x_v, dv, du, edge_order=2)
    y_vv, _ = np.gradient(y_v, dv, du, edge_order=2)
    z_vv, _ = np.gradient(z_v, dv, du, edge_order=2)

    Xuu = np.stack((x_uu, y_uu, z_uu), axis=-1)
    Xuv = np.stack((x_uv, y_uv, z_uv), axis=-1)
    Xvv = np.stack((x_vv, y_vv, z_vv), axis=-1)

    L = np.einsum('ijk,ijk->ij', normals, Xuu)
    M = np.einsum('ijk,ijk->ij', normals, Xuv)
    N = np.einsum('ijk,ijk->ij', normals, Xvv)

    return L, M, N
