import numpy as np

def parametrize_helicoid(a=1.0, b=1.0, u_range=(-2*np.pi, 2*np.pi), v_range=(-1, 1), num_points=100):

    u = np.linspace(u_range[0], u_range[1], num_points)
    v = np.linspace(v_range[0], v_range[1], num_points)
    u, v = np.meshgrid(u, v)

    x = a * v * np.cos(u)
    y = a * v * np.sin(u)
    z = b * u

    return x, y, z, u, v
