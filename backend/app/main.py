from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, budgets, expenses, incomes, categories
from .database import engine, Base
from .seeders.category import seed_categories
from sqlalchemy.orm import Session
from .database import SessionLocal

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Define frontend as allowed origin
origins = [
    "http://localhost:3000",  # React dev
    "http://127.0.0.1:3000",  # React dev
]

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(users.router)
app.include_router(budgets.router)
app.include_router(expenses.router)
app.include_router(incomes.router)
app.include_router(categories.router)

# Initialize the database and seed predefined categories
def init_db():
    db: Session = SessionLocal()
    seed_categories(db)
    db.close()

# Call init_db when the application starts
@app.on_event("startup")
def on_startup():
    init_db()