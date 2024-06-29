from fastapi import FastAPI, HTTPException
from .database import database, engine, metadata
from .models import users

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/")
async def read_users():
    query = users.select()
    return await database.fetch_all(query)



@app.post("/users/")
async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    last_record_id = await database.execute(query)
    return {**{"id": last_record_id}, "name": name, "email": email}



@app.get("/")
async def root():
    return "root"