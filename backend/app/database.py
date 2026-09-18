import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not configured")

if not MONGODB_DATABASE:
    raise RuntimeError("MONGODB_DATABASE is not configured")

client = MongoClient(MONGODB_URI)
database = client[MONGODB_DATABASE]


def check_database_connection() -> bool:
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False