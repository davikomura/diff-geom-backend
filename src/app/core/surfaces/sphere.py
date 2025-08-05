import numpy as np

def parametrize_sphere(a=1.0, num_points=100):
    
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(-np.pi / 2, np.pi / 2, num_points)
    u, v = np.meshgrid(u, v)

    x = a * np.cos(v) * np.cos(u)
    y = a * np.cos(v) * np.sin(u)
    z = a * np.sin(v)

    return x, y, z, u, v
