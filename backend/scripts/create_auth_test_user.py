from datetime import datetime, timezone
from uuid import uuid4

from app.auth import hash_password
from app.database import database


users_collection = database["users"]

test_users = [
    {
        "id": str(uuid4()),
        "email": "test-non-admin@example.com",
        "password_hash": hash_password("TestPassword123!"),
        "role": "user",
        "status": "active",
        "created_at": datetime.now(timezone.utc),
    },
    {
        "id": str(uuid4()),
        "email": "test-inactive@example.com",
        "password_hash": hash_password("TestPassword123!"),
        "role": "admin",
        "status": "inactive",
        "created_at": datetime.now(timezone.utc),
    },
]


for user in test_users:
    existing_user = users_collection.find_one({"email": user["email"]})

    if existing_user:
        print(f"Already exists: {user['email']}")
        continue

    users_collection.insert_one(user)
    print(f"Created: {user['email']}")