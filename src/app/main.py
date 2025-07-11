from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.curve import router as curve_router

app = FastAPI(title="Differential Geometry Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://diff-geom-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(curve_router)