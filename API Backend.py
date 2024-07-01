# Code FastAPI pour les endpoints
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import databases, sqlalchemy

DATABASE_URL = "mysql+aiomysql://user:password@localhost/job_board"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str
    source: str
    date_posted: str

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/jobs/", response_model=List[Job])
async def read_jobs():
    query = "SELECT * FROM jobs"
    return await database.fetch_all(query)
