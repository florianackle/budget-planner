from pytest import fixture
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base
from app.dependencies import get_db
from app.seeders.category import seed_categories
from app.models.user import User
from app.services.user_service import get_password_hash


@fixture()
def db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app_test.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db_session = TestingSessionLocal()

    # Rebuild the test database
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Seed categories after initializing the database
    seed_categories(db_session)

    def override_get_db():
        try:
            db = db_session
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    return db_session


@fixture()
def client(db):
    return TestClient(app)


@fixture()
def user_homer(db):
    # Create a user with a hashed password using the get_password_hash from user_service
    hashed_password = get_password_hash("1234")
    user = User(username="homer", hashed_password=hashed_password)
    db.add(user)
    db.commit()
    return user


@fixture()
def user_homer_authenticated(client, user_homer):
    # Simulate login to get access token for the user "Homer"
    response = client.post("/users/login", json={"username": user_homer.username, "password": "1234"})
    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]
    return user_homer, access_token


@fixture()
def client_authenticated(client, user_homer_authenticated):
    # Apply the access token to each request made by the client
    user, access_token = user_homer_authenticated

    def authenticated_request(method, url, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {access_token}"
        return client.request(method, url, headers=headers, **kwargs)

    return authenticated_request
