from ..services.duckduckgo import DuckDuckGoService
from ..services.llm import LLMService

class SearchInteractor:
    def __init__(self):
        self.duck_service = DuckDuckGoService()
        self.llm_service = LLMService()

    async def execute(self, question: str) -> str:
        # Get search results
        search_results = await self.duck_service.search(question)
        
        # Get LLM response
        response = await self.llm_service.get_answer(question, search_results)
        
        return response