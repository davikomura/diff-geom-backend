from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.surface import router as surface_router

app = FastAPI(title="Differential Geometry Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://diff-geom-frontend.vercel.app"],
    # allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(surface_router)