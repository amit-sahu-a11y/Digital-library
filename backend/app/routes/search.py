from fastapi import APIRouter

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("/")
def test_search():

    return {
        "message": "Search API is working!"
    }