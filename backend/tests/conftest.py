import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base
from app.dependencies import get_db
from app.seeders.category import seed_categories

# Setup für die Test-Datenbank
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override der Datenbank-Abhängigkeit für Tests
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    # Erstellen der Test-Datenbank und Seeding der Kategorien
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    seed_categories(db)
    db.commit()
    db.close()

    # Client für Tests
    with TestClient(app) as c:
        yield c

    # Test-Datenbank nach Tests löschen
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client_authenticated(client):
    # Authentifizierter Client mit registriertem Benutzer
    response = client.post("/users/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 201

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpassword"})
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    client.headers["Authorization"] = f"Bearer {token}"
    return client
