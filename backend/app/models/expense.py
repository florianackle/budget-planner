from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    owner = relationship("User", back_populates="expenses")
    budget = relationship("Budget", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
