from fastapi import FastAPI
from app.routes.upload import router

app = FastAPI(
    title="ScholarSync MVP"
)

app.include_router(router)