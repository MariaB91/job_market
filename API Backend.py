from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import databases, sqlalchemy

DATABASE_URL = "mysql+aiomysql://user:password@localhost/job_board"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

router = APIRouter()

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str
    source: str
    date_posted: str

@router.on_event("startup")
async def startup():
    await database.connect()

@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@router.get("/jobs/", response_model=List[Job])
async def read_jobs():
    query = "SELECT * FROM jobs"
    return await database.fetch_all(query)
