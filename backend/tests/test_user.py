import pytest
from fastapi import status

def test_register_user(client):
    # Test für die Benutzerregistrierung
    response = client.post("/users/", json={"username": "newuser", "password": "newpassword"})
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == "newuser"


def test_login_user(client):
    # Erst Benutzer registrieren
    client.post("/users/", json={"username": "newuser", "password": "newpassword"})

    # Test für das Login
    response = client.post("/users/login", data={"username": "newuser", "password": "newpassword"})
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()

def test_login_user_wrong_password(client):
    # Erst Benutzer registrieren
    client.post("/users/", json={"username": "newuser", "password": "newpassword"})

    # Test für das Login mit falschem Passwort
    response = client.post("/users/login", data={"username": "newuser", "password": "wrongpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "access_token" not in response.json()
