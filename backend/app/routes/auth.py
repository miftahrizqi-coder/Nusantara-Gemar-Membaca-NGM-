from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel


from app.auth import get_current_admin
from app.auth import create_access_token, verify_password
from app.user_repository import find_user_by_email


router = APIRouter(prefix="/auth", tags=["authentication"])


class LoginRequest(BaseModel):
    email: str
    password: str

@router.get("/me")
def get_me(user: dict = Depends(get_current_admin)):
    return {
        "id": user["id"],
        "email": user["email"],
        "role": user["role"],
        "status": user["status"],
    }

@router.post("/login")
def login(request: LoginRequest):
    user = find_user_by_email(request.email.lower())

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    if user.get("status") != "active":
        raise HTTPException(
            status_code=403,
            detail="User is inactive",
        )

    if not verify_password(request.password, user["password_hash"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        user_id=user["id"],
        role=user["role"],
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }