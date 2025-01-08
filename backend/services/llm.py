from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import List
import os

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant focused on providing current information. Use the search results to provide up-to-date information. Be concise and specific in your response."),
            ("user", "Question: {question}\n\nSearch Results: {search_results}")
        ])
        
        self.output_parser = StrOutputParser()

    async def get_answer(self, question: str, search_results: List[str]) -> str:
        try:
            if not search_results:
                return "I couldn't find any current information for your question. Please try rephrasing it."

            chain = self.prompt | self.llm | self.output_parser
            
            formatted_results = "\n".join(search_results)
            
            response = await chain.ainvoke({
                "question": question,
                "search_results": formatted_results
            })
            
            return response.strip()
            
        except Exception as e:
            return f"Error generating response: {str(e)}"