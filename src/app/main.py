from fastapi import FastAPI
from app.api.curve import router as curve_router

app = FastAPI(title="Differential Geometry Simulator")

app.include_router(curve_router)