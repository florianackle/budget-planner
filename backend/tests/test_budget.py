def test_create_budget(client_authenticated):
    # Try to create a budget for Homer
    response = client_authenticated("POST", "/budget/", json={"username": "homer"})
    assert response.status_code == 200
    data = response.json()

    assert data["owner_id"] == 1  # Homer has user_id = 1
    assert "id" in data  # Check if budget ID is present


def test_read_budget(client_authenticated):
    # First, create a budget for Homer
    response = client_authenticated("POST", "/budget/", json={"username": "homer"})
    assert response.status_code == 200
    budget_id = response.json()["id"]

    # Now try to read the budget
    response = client_authenticated("GET", "/budget/")
    assert response.status_code == 200
    data = response.json()

    assert data["owner_id"] == 2  # Homer has user_id = 1
    assert data["id"] == budget_id  # Check if the correct budget is returned
