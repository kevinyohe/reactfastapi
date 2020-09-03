from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.1.131:3000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_items():
    return [
        {"url": "https://news.ycombinator.com", "title": "https://news.ycombinator.com/", "points": 23342},
        {"url": "https://kevinyohe.dev", "title": "kevinyohe.dev", "points": 283933},
        {"url": "https://docker.com", "title": "Docker", "points": 3},
            ]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
