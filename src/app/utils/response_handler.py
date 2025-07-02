from typing import Callable, Dict, Any, Tuple
import numpy as np
from app.core.geometry_curve import compute_curve_data
from app.utils.response_builder import build_surface_response

def handle_surface_request(
    parametrization_fn: Callable[[], Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]],
    curvature_type: str = "gaussian",
    a: float = 1.0,
    b: float = 1.0
) -> Dict[str, Any]:
    x, y, z, u, v = parametrization_fn()
    result = compute_curve_data(x, y, z, u, v, curvature_type=curvature_type, a=a, b=b)

    if isinstance(result, dict):
        return {
            "coordinates": {
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist()
            },
            "principal_curvatures": {
                "k1": result["k1"].tolist(),
                "k2": result["k2"].tolist()
            }
        }

    return build_surface_response(x, y, z, result)
