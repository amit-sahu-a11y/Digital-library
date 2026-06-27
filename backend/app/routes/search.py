from fastapi import APIRouter

from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

search_service = SearchService()


@router.get("/")
def search(query: str):

    results = search_service.search(query)

    return results