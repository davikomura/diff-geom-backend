from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Dict, Any

from app.core.surfaces.registry import surface_parametrizations
from app.utils.response_handler import handle_surface_request
from app.schemas.surface import SurfaceRequest
from app.data.surface_info import surface_info

router = APIRouter(prefix="/surface", tags=["Surface"])

@router.get("/")
def surface(request: SurfaceRequest = Depends()) -> Dict[str, Any]:
    fn = surface_parametrizations.get(request.surface)
    if not fn:
        raise HTTPException(status_code=400, detail=f"Unsupported surface type: {request.surface}")

    return handle_surface_request(
        parametrization_fn=fn,
        curvature_type=request.curvature,
        a=request.a,
        b=request.b
    )
    
@router.get("/info")
def get_surface_info(surface: str = Query(..., description="Nome da superfície")):
    if surface not in surface_info:
        raise HTTPException(status_code=404, detail=f"Superfície '{surface}' não encontrada.")
    return surface_info[surface]