import inspect
from typing import Callable, Dict, Any, Tuple
import numpy as np
from app.core.geometry_surface import compute_surface_data
from app.utils.response_builder import build_surface_response

def handle_surface_request(
    parametrization_fn: Callable[..., Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]],
    curvature_type: str = "gaussian",
    a: float = 1.0,
    b: float = 1.0
) -> Dict[str, Any]:
    sig = inspect.signature(parametrization_fn)
    kwargs = {}
    if 'a' in sig.parameters:
        kwargs['a'] = a
    if 'b' in sig.parameters:
        kwargs['b'] = b

    x, y, z, u, v = parametrization_fn(**kwargs)
    result = compute_surface_data(x, y, z, u, v, curvature_type=curvature_type, a=a, b=b)

    response = {
        "coordinates": {
            "x": x.tolist(),
            "y": y.tolist(),
            "z": z.tolist()
        }
    }

    if curvature_type == "principal" and isinstance(result[3], dict):
        response["principal_curvatures"] = {
            "k1": result[3]["k1"].tolist(),
            "k2": result[3]["k2"].tolist()
        }
    else:
        response["curvature"] = np.array(result[3]).tolist()

    return response