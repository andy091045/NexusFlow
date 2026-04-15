# app/schemas/user.py
from pydantic import BaseModel


class UserCreate(BaseModel):       # 註冊時前端送進來的格式
    username: str
    email: str
    password: str


class UserResponse(BaseModel):     # 回傳給前端的格式（不含密碼）
    id: int
    username: str
    email: str
    disabled: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
