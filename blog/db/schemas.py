from typing import List, Optional

from pydantic import BaseModel, EmailStr


class CommentBase(BaseModel):
    author: str
    body: str
    post: str
    created_at: str


class CommentCreate(CommentBase):
    pass


class Comment(BaseModel):
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    body: str
    author: str
    image: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: str
    updated_at: str
    comment: List[Comment]

    class Config:
        orm_mode = True


class BaseUser(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None


class UserCreate(BaseUser):
    email: EmailStr
    password: str


class UserUpdate(BaseUser):
    password: Optional[str] = None


class User(BaseUser):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
