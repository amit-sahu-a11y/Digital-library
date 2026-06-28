from fastapi import APIRouter
from typing import Optional

from app.services.search_service import SearchService

router = APIRouter()

search_service = SearchService()


@router.get("/search")
def search(
    query: str,
    top_k: int = 5,
    document_id: Optional[str] = None
):

    return search_service.search(
        query=query,
        top_k=top_k,
        document_id=document_id
    )