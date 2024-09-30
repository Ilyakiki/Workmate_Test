import uvicorn
from fastapi import FastAPI, Depends, Query
from fastapi import APIRouter
from typing import Optional,List
from schema import Cat, Breed


app = FastAPI()


@app.get("/")
async def test():
    return {"Hello": "World"}


@app.get("/breeds")
async def get_list_of_breeds() -> List[Breed]:
    ...
    return ["Breed1", "Breed2", "Breed3"]


@app.get("/cats")
async def get_list_cats() -> List[Cat]:
    ...
    return ["Cat1", "Cat2", "Cat3"]

@app.get("/cats")
async def get_cats_by_breed(breeds: List[str] = Query([]),) -> List[Cat]:
    return breeds

@app.get("/cats/{id}")
async def get_cat_by_id(id: int) -> Cat:
    return id

@app.post("/cats")
async def create_cat(cat: Cat) -> str:
    return cat

@app.put("/cats/{id}")
async def update_cat(id: int, cat: Cat):
    return cat

@app.delete("/cats/{id}")
async def delete_cat(id: int):
    return id



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)