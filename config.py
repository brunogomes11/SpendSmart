import os

SECRET_KEY = os.getenv("SECRET_KEY", "57e8d872962c4ca7ab136255d0c0e33e")
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", "postgresql://localhost/expense_tracker"
)
