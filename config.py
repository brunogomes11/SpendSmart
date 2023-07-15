import os

SECRET_KEY = os.getenv("SECRET_KEY", "anything")
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", "postgresql://localhost/expense_tracker"
)
