from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from blog.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    name = Column(String, unique=True)

    post = relationship('Post', back_populates='author')
    comment = relationship('Comment', back_populates='author')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(Text)
    image = Column(String, default='...')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship('User', back_populates='post')
    comment = relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    created_at = Column(DateTime)
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship('Post', back_populates='comment')
    author = relationship('User', back_populates='comment')


