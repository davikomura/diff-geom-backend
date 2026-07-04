import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np
from app.core.surfaces.sphere import parametrize_sphere
from app.core.geometry_surface import compute_surface_data

def test_sphere_curvature():
    a = 2.0
    x, y, z, u, v = parametrize_sphere(a=a, num_points=50)
    
    # Compute surface data (Gaussian curvature)
    _, _, _, K = compute_surface_data(x, y, z, u, v, curvature_type="gaussian")
    
    # The Gaussian curvature of a sphere of radius a is exactly 1 / a^2
    expected_K = 1.0 / (a ** 2) # should be 1 / 4 = 0.25
    
    # Assert correctness
    assert np.allclose(K, expected_K, atol=1e-2), f"Gaussian curvature calculation failed! Max diff: {np.max(np.abs(K - expected_K))}"
    print("Success: Sphere Gaussian curvature matches theory perfectly!")

if __name__ == "__main__":
    test_sphere_curvature()
