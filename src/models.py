import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120))
    email = Column(String(120), nullable=False)
    password = Column(String(250), nullable=False)


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(Users)

    def to_dict(self):
        return {}


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(Users)

    def to_dict(self):
        return {}


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship(Posts)

    def to_dict(self):
        return {}


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship(Posts, foreign_keys=[post_id])
    author = relationship(Users, foreign_keys=[author_id])

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
