from typing import Literal
from pydantic import BaseModel, Field

class SurfaceRequest(BaseModel):
    surface: Literal[
        "sphere", "torus", "enneper", "helicoid", "hyperbolic_paraboloid", "elliptic_paraboloid"
    ] = Field("sphere", description="Tipo da superfície")
    
    curvature: Literal["gaussian", "mean", "principal", "normal"] = Field(
        "gaussian", description="Tipo de curvatura"
    )

    a: float = Field(1.0, description="Parâmetro A da superfície")
    b: float = Field(1.0, description="Parâmetro B da superfície")
