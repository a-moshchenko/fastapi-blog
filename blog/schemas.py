from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Comment(BaseModel):
    author: str
    body: str
    post: str
    date: str


class Post(BaseModel):
    title: str
    body: str
    author: str
    create_on: str
    update_on: str
    file_path: str
    comments: Optional[List[Comment]]


class BaseUser(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(BaseUser):
    email: EmailStr
    password: str


class UserUpdate(BaseUser):
    password: Optional[str] = None
