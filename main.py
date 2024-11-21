from fastapi import FastAPI
from domain.library import library_router

app = FastAPI()

app.include_router(library_router.router)