import uvicorn
from fastapi import FastAPI, Depends, Query
from fastapi import APIRouter
from typing import Optional,List

from sqlalchemy import select,insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import init_database,get_async_session
from schema import Cat, Breed
from models import Cat as cat, Breed as breed


app = FastAPI()




@app.on_event("startup")
async def startup():
    await init_database()

@app.get("/")
async def test():
    return {"Hello": "World"}


@app.get("/breeds")
async def get_list_of_breeds(session:AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(breed))
    breeds = [row.name for row in result.scalars()]
    return breeds

@app.post("/breeds")
async def add_breed(br : Breed, session : AsyncSession = Depends(get_async_session),):
    await session.execute(insert(breed).values(name=br.name))
    await session.commit()
    return 'ok'

@app.get("/cats")
async def get_list_cats() -> List[Cat]:
    ...
    return ["Cat1", "Cat2", "Cat3"]

@app.get("/cats")
async def get_cats_by_breed(breeds: List[str] = Query([]),) -> List[Cat]:
    return breeds

@app.get("/cats/{id}")
async def get_cat_by_id(id: int,session:AsyncSession = Depends(get_async_session)) -> Cat:
    result = await session.execute(select(breed).where(eq))
    return result.scalars().first()

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