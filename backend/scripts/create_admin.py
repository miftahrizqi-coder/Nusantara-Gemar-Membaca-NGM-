import getpass
from datetime import datetime, timezone
from uuid import uuid4

from app.auth import hash_password
from app.database import database
from app.user_repository import find_user_by_email


def main():
    email = input("Admin email: ").strip().lower()
    password = getpass.getpass("Admin password: ")

    if not email:
        raise ValueError("Email is required")

    if not password:
        raise ValueError("Password is required")

    existing_user = find_user_by_email(email)

    if existing_user:
        raise ValueError("User with this email already exists")

    user = {
        "id": str(uuid4()),
        "email": email,
        "password_hash": hash_password(password),
        "role": "admin",
        "status": "active",
        "created_at": datetime.now(timezone.utc),
    }

    database["users"].insert_one(user)

    print("Admin user created successfully.")


if __name__ == "__main__":
    main()