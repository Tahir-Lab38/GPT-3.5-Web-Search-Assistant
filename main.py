from fastapi import FastAPI
from backend.routes.search import router as search_router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Include routers
app.include_router(search_router, prefix="/api", tags=["search"])