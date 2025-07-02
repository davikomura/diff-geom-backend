from pydantic import BaseModel

class CurveInput(BaseModel):
    x: str
    y: str
    z: str
    u: str
    v: str
    num_points: int = 100
