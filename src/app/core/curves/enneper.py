import numpy as np

def parametrize_enneper(range_u=2.0, num_points=100):

    u = np.linspace(-range_u, range_u, num_points)
    v = np.linspace(-range_u, range_u, num_points)
    u, v = np.meshgrid(u, v)

    x = u - (u**3)/3 + u*v**2
    y = - v + (v**3)/3 - v*u**2
    z = u**2 - v**2

    return x, y, z, u, v
