from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
from simple_model import get_recommendations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from dotenv import load_dotenv
load_dotenv()  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class RecommendationRequest(BaseModel):
    movie_ids: List[int]

class GenreRecommendationRequest(BaseModel):
    genres: List[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/genre")
async def recommend_genres(data: GenreRecommendationRequest):
    try:
        recommendations = get_recommendations(data.genres)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

import os
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
