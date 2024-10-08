from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # A user can only have one budget
    budget = relationship("Budget", back_populates="owner", uselist=False)  # no 'budgets' because there is only one
    expenses = relationship("Expense", back_populates="owner")
    incomes = relationship("Income", back_populates="owner")
