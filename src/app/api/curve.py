from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Dict, Any

from app.core.curves.registry import curve_parametrizations
from app.utils.response_handler import handle_surface_request
from app.schemas.curve import CurveRequest
from app.data.curve_info import curve_info

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
    
@router.get("/info")
def get_curve_info(curve: str = Query(..., description="Nome da curva ou superfície")):
    if curve not in curve_info:
        raise HTTPException(status_code=404, detail=f"Curva '{curve}' não encontrada.")
    return curve_info[curve]