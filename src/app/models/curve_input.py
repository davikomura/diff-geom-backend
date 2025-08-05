from pydantic import BaseModel

class SurfaceInput(BaseModel):
    x: str
    y: str
    z: str
    u: str
    v: str
    num_points: int = 100
