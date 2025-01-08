from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..interactors.search import SearchInteractor

router = APIRouter()

class SearchResponse(BaseModel):
    answer: str

@router.get("/search", response_model=SearchResponse)
async def search(question: str):
    try:
        interactor = SearchInteractor()
        answer = await interactor.execute(question)
        return SearchResponse(answer=answer)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
