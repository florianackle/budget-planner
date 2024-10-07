# main.py
from fastapi import FastAPI
from .routers import users, budgets, expenses, incomes, categories
from .database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(budgets.router)
app.include_router(expenses.router)
app.include_router(incomes.router)
app.include_router(categories.router)
