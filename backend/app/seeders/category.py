from sqlalchemy.orm import Session
from ..models.category import Category


def seed_categories(db: Session):
    categories = [
        {"name": "Allgemein"},
        {"name": "Lohn"},
        {"name": "Essen"},
        {"name": "Auto"},
        {"name": "Versicherungen"},
        {"name": "Haushalt"},
        {"name": "Hobby"},
        {"name": "Freizeit"},
        {"name": "Transport"},
        {"name": "Kleidung"},
        {"name": "Bildung"},
        {"name": "Gesundheit"},
        {"name": "Spenden"},
        {"name": "Technologie"},
        {"name": "Reisen"},
        {"name": "Unterhaltung"},
        {"name": "Kommunikation"},
        {"name": "Versorgungsunternehmen"},
        {"name": "Bürobedarf"},
        {"name": "Fitness"},
        {"name": "Kinderbetreuung"},
        {"name": "Investitionen"},
        {"name": "Haustiere"},
    ]

    for category in categories:
        db_category = db.query(Category).filter_by(name=category["name"]).first()
        if not db_category:
            new_category = Category(name=category["name"])
            db.add(new_category)
    db.commit()
