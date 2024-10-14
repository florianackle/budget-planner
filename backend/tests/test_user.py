import pytest

# Test for user registration
def test_user_registration(client):
    response = client.post("/users/", json={
        "email": "testuser@budget.com",
        "password": "testpassword"
    })
    assert response.status_code == 201  # Registration should return a 201 Created
    data = response.json()
    assert data["email"] == "testuser@budget.com"
    assert "id" in data  # Ensure user ID is returned

# Test for user login with registered user
def test_user_login(client, user):
    response = client.post("/login/", json={
        "email": "testuser@budget.com",
        "password": "testpassword"
    })
    assert response.status_code == 200  # Login should return 200 OK
    data = response.json()
    assert "access_token" in data  # Check if JWT token is returned

# Test for incorrect password
def test_user_login_wrong_password(client, user):
    response = client.post("/login/", json={
        "email": "testuser@budget.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401  # Login should fail with a 401 Unauthorized
    data = response.json()
    assert data["detail"] == "Incorrect email or password"
