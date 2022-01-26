import asyncio
from uvicorn import Server, Config
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from blog.db import schemas, models, crud
from blog.db.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    config = Config(app=app, loop=loop, host='0.0.0.0', port=5000)
    server = Server(config)
    loop.run_until_complete(server.serve())

