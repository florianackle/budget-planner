def test_create_user(client):
    response = client.post(
        "/users/",
        json={"username": "bart", "password": "chimichangas4life"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "bart"
    assert "id" in data


def test_no_password_returned(client):
    response = client.post(
        "/users/",
        json={"username": "homer", "password": "chimichangas4life"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "homer"
    assert "password" not in data


def test_unique_username(client):
    # Create the first user
    response = client.post(
        "/users/",
        json={"username": "homer", "password": "chimichangas4life"},
    )
    assert response.status_code == 200

    # Try to create a second user with the same username
    response = client.post(
        "/users/",
        json={"username": "homer", "password": "anotherpassword"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Username already registered"


def test_login_user(client):
    # Register a new user
    client.post(
        "/users/",
        json={"username": "homer", "password": "chimichangas4life"},
    )

    # Test login with correct credentials
    response = client.post(
        "/users/login",
        json={"username": "homer", "password": "chimichangas4life"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data