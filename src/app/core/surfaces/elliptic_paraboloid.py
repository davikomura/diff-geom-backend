import numpy as np

def parametrize_elliptic_paraboloid(a=1.0, b=1.0, u_range=(-1, 1), v_range=(-1, 1), num_points=100):
    
    u = np.linspace(u_range[0], u_range[1], num_points)
    v = np.linspace(v_range[0], v_range[1], num_points)
    u, v = np.meshgrid(u, v)

    x = u
    y = v
    z = (u ** 2) / (a ** 2) + (v ** 2) / (b ** 2)

    return x, y, z, u, v