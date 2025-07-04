from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any

from app.core.curves.registry import curve_parametrizations
from app.utils.response_handler import handle_surface_request
from app.schemas.curve import CurveRequest

router = APIRouter(prefix="/curve", tags=["Curve"])

@router.get("/")
def curve(request: CurveRequest = Depends()) -> Dict[str, Any]:
    fn = curve_parametrizations.get(request.curve)
    if not fn:
        raise HTTPException(status_code=400, detail=f"Unsupported curve type: {request.curve}")
    
    return handle_surface_request(
        parametrization_fn=fn,
        curvature_type=request.curvature,
        a=request.a,
        b=request.b
    )