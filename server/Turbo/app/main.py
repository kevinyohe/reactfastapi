from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pymongo import MongoClient
from typing import Dict
from bson.objectid import ObjectId

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['demo']
demodocs = db['demodocs']
#demodocs.delete_one({"name": "Kevin"})
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
    results = []
    items = demodocs.find({})
    for item in items:
        item['_id'] = str(item['_id'])
        results.append(item)
    return results

    return [
        {"url": "https://news.ycombinator.com", "title": "https://news.ycombinator.com/", "points": 23342},
        {"url": "https://kevinyohe.dev", "title": "kevinyohe.dev", "points": 283933},
        {"url": "https://docker.com", "title": "Docker", "points": 3},
            ]


@app.post("/items/")
async def create_item(item: Dict):
    demodocs.insert_one(item)
    return str(item)


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    demodocs.delete_one({'_id': ObjectId(item_id)})
    return {"msg": "deleted item"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
