from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..interactors.search import SearchInteractor

router = APIRouter()

class SearchRequest(BaseModel):
    question: str

class SearchResponse(BaseModel):
    answer: str

@router.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    try:
        interactor = SearchInteractor()
        answer = await interactor.execute(request.question)
        return SearchResponse(answer=answer)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))