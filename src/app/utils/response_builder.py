import numpy as np
from typing import Any, Dict

def convert_to_serializable(data: Any) -> Any:
    if isinstance(data, np.ndarray):
        return data.tolist()
    elif isinstance(data, dict):
        return {k: convert_to_serializable(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple)):
        return [convert_to_serializable(v) for v in data]
    else:
        return data

def build_surface_response(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    curvature_data: Any,
    curvature_type: str = "gaussian"
) -> Dict[str, Any]:
    response = {
        "coordinates": {
            "x": convert_to_serializable(x),
            "y": convert_to_serializable(y),
            "z": convert_to_serializable(z)
        }
    }

    if curvature_type == "principal" and isinstance(curvature_data, dict):
        response["principal_curvatures"] = convert_to_serializable(curvature_data)
    else:
        response[f"{curvature_type}_curvature"] = convert_to_serializable(curvature_data)

    return response
