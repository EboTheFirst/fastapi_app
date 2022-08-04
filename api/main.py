from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    if crud.get_item(db, item_id=item.id):
        raise HTTPException(status_code=400, detail="Item id already exists in database")
    return crud.create_item(db, item=item)


@app.put("/items/", response_model=schemas.Item)
def update_item(item: schemas.Item, db: Session = Depends(get_db)):
    if not crud.get_item(db, item_id=item.id):
        raise HTTPException(status_code=400, detail="Nothing to update: Item does not exist")
    return crud.update_item(db, item=item)

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/item/{id}", response_model=schemas.Item)
def read_items(item_id:int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=400, detail="Item does not exist")
    return item
