from fastapi import FastAPI
from pydantic import BaseModel
from app.db.database import Base, engine
from dotenv import load_dotenv
from app.models import *

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

class Person(BaseModel):
    name: str
    email:str

@app.post("/person")
async def create_person(person: Person):
    return person