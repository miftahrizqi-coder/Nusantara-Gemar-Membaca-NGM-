from datetime import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    email: EmailStr
    role: str
    status: str
    created_at: datetime