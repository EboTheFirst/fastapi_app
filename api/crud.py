from sqlalchemy.orm import Session

from . import models, schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def update_item(db: Session, item: schemas.Item):
    db.query(models.Item).filter_by(id=item.id).update({
        "name":item.name,
        "weight":item.weight,
        "description":item.description,
        })
    db.commit()
    return item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.Item):
    db_item = models.Item(id=item.id, name=item.name, weight=item.weight, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

