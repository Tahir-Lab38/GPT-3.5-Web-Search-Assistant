from duckduckgo_search import DDGS
from typing import List
import asyncio

class DuckDuckGoService:
    def __init__(self):
        self.ddgs = DDGS()

    async def search(self, query: str) -> List[str]:
        try:
            # Enhance query for current information
            enhanced_query = f"current {query} latest update"
            
            # Perform the search
            results = []
            search_results = self.ddgs.text(enhanced_query, max_results=3)
            
            # Process results
            for r in search_results:
                if isinstance(r, dict) and 'body' in r:
                    results.append(r['body'])
                
            if not results:
                return ["No current information found. Please try a different search query."]
                
            return results
            
        except Exception as e:
            return [f"An error occurred during search: {str(e)}"]