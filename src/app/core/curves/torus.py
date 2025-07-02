import numpy as np

def parametrize_torus(a=2.0, b=0.5, c=0.5, num_points=100):
   
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, 2 * np.pi, num_points)
    u, v = np.meshgrid(u, v)

    x = (a + b * np.cos(v)) * np.cos(u)
    y = (a + b * np.cos(v)) * np.sin(u)
    z = c * np.sin(v)

    return x, y, z, u, v
