from fastapi import FastAPI

from app.routes.upload import router as upload_router
from app.routes.search import router as search_router

app = FastAPI(
    title="ScholarSync MVP"
)

app.include_router(upload_router)
app.include_router(search_router)