from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import Income, Expense, Budget


class BudgetCalculator:
    @staticmethod
    def calculate_total_amount(db: Session, user_id: int):
        # Calc sum of incomes
        total_income = db.query(func.sum(Income.amount)).filter(Income.owner_id == user_id).scalar() or 0

        # Calc sum of expenses
        total_expense = db.query(func.sum(Expense.amount)).filter(Expense.owner_id == user_id).scalar() or 0

        # Calc budget (Incomes - Expenses)
        total_amount = total_income - total_expense

        # Find budget of user
        db_budget = db.query(Budget).filter(Budget.owner_id == user_id).first()
        if db_budget:
            db_budget.total_amount = total_amount
            db.commit()
            db.refresh(db_budget)
        return db_budget
