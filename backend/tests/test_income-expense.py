import pytest

# Use the client_authenticated fixture from conftest.py
@pytest.mark.usefixtures("client_authenticated")
def test_create_income_and_expense(client_authenticated):
    # 1. Create a budget for "homer"
    response = client_authenticated("POST", "/budget/", json={"username": "homer"})
    assert response.status_code == 200
    budget_id = response.json()["id"]

    # 2. Add income: description="Lohn Oktober", amount=4000, with budget_id and category_id
    income_data = {
        "description": "Lohn Oktober",
        "amount": 4000,
        "category_id": 2,  # category_id for "Lohn"
        "budget_id": budget_id  # Link to budget
    }
    response_income = client_authenticated("POST", "/incomes/", json=income_data)
    assert response_income.status_code == 200

    # 3. Add expense: description="Mittagessen", amount=50, with budget_id and category_id
    expense_data = {
        "description": "Mittagessen",
        "amount": 50,
        "category_id": 3,  # category_id for "Essen"
        "budget_id": budget_id  # Link to budget
    }
    response_expense = client_authenticated("POST", "/expenses/", json=expense_data)
    assert response_expense.status_code == 200

    # 4. Fetch the updated budget and verify the total amount
    response_budget = client_authenticated("GET", "/budget/")
    assert response_budget.status_code == 200
    updated_budget = response_budget.json()

    # Verify the total amount: 4000 income - 50 expenses = 3950
    assert updated_budget["total_amount"] == 3950
