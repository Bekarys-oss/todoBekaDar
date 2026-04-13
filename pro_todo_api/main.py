from fastapi import APIRouter, Depends, HTTPException, FastAPI
from database import Base, engine
from routers import auth
from routers import tasks

Base.metadata.create_all(bind=engine)
app = FastAPI(title = "Todo API with Authentication")
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get ("/")
def read_root():
    return {"massage": "Welcome to the Todo API with Authentication"}