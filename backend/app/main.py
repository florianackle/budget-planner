from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_root(db: Session = Depends(get_db)):
    return {"Hello": "World"}
