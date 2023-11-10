from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routers.movies_router import router as movies_router

app = FastAPI()

cors_origins = [
    'http://localhost:5173',
    'http://localhost:4173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movies_router)


@app.get("/")
def home():
    return RedirectResponse('/docs', status_code=status.HTTP_302_FOUND)
