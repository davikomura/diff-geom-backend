import numpy as np
from typing import Any, Dict

def convert_to_serializable(data: Any) -> Any:
    if isinstance(data, np.ndarray):
        return data.tolist()
    return data

def build_surface_response(x: np.ndarray, y: np.ndarray, z: np.ndarray, K: np.ndarray) -> Dict[str, Any]:
    return {
        "coordinates": {
            "x": convert_to_serializable(x),
            "y": convert_to_serializable(y),
            "z": convert_to_serializable(z)
        },
        "gaussian_curvature": convert_to_serializable(K)
    }
