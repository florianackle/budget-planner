from pytest import fixture
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app
from app.dependencies import get_db
from fastapi.testclient import TestClient

from app.models.income import Income
from app.models.expense import Expense
from app.models.user import User


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

    # Drop and recreate tables before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Override the get_db dependency to use the test database
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
    # Return a test client using the FastAPI app with overridden dependencies
    return TestClient(app)

@fixture()
def client_authenticated(client, user_authenticated):
    user, access_token = user_authenticated
    client.headers["Authorization"] = f"Bearer {access_token}"
    return client


@fixture()
def user(db):
    # Create a test user with a hashed password
    user = User(email="testuser@budget.com", hashed_password=_hash_password("testpassword"))
    db.add(user)
    db.commit()
    return user


@fixture()
def user_authenticated(client, user):
    # Authenticate the test user and return the user along with the access token
    response = client.post("/login/", json={"email": user.email, "password": "testpassword"})
    assert response.status_code == 200
    data = response.json()
    access_token = data["access_token"]
    return user, access_token


@fixture()
def income_for_user(user, db):
    # Create test income for the user
    income = Income(amount=5000, description="Salary", user_id=user.id)
    db.add(income)
    db.commit()
    return income


@fixture()
def expense_for_user(user, db):
    # Create test expenses for the user
    expense = Expense(amount=1000, description="Rent", user_id=user.id)
    db.add(expense)
    db.commit()
    return expense
