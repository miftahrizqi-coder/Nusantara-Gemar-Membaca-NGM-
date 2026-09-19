from app.database import database

users_collection = database ["users"]

def find_user_by_email(email:str):
    return users_collection.find_one({"email":email})

def find_user_by_id(user_id:int):
    return users_collection.find_one({"id":user_id})