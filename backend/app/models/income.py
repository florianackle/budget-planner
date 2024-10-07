from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    owner = relationship("User", back_populates="incomes")
    budget = relationship("Budget", back_populates="incomes")
    category = relationship("Category", back_populates="incomes")
