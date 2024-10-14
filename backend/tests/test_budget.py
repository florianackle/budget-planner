def test_create_budget(client_authenticated):
    # Try to create a budget for Homer
    response = client_authenticated("POST", "/budget/", json={"username": "homer"})
    assert response.status_code == 201  # Expect 201 Created
    data = response.json()
    assert data["owner"]["username"] == "homer"  # Check if budget belongs to Homer
    assert "id" in data  # Check if budget ID is present


def test_read_budget(client_authenticated):
    # First, create a budget for Homer
    response = client_authenticated("POST", "/budget/", json={"username": "homer"})
    assert response.status_code == 201
    budget_id = response.json()["id"]

    # Now try to read the budget
    response = client_authenticated("GET", "/budget/")
    assert response.status_code == 200  # Expect 200 OK
    data = response.json()
    assert data["id"] == budget_id  # Check if the correct budget is returned
    assert data["owner"]["username"] == "homer"  # Ensure the owner is Homer
