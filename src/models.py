import os
import sys
import eralchemy2
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    created = Column(String(30))
    edited = Column(String(30))
    name = Column(String(20), nullable=False)
    homeworld = Column(String(20))
    url = Column(String(20))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)
    created = Column(String(20))
    edited = Column(String(20))
    name = Column(String(20))
    url = Column(String(20))


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(20))
    starship_class = Column(String(20))
    manufacturer = Column(String(20))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    MGLT = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(20))
    pilots = Column(String(20))
    created = Column(String(25))
    edited = Column(String(250))
    name = Column(String(20))
    url = Column(String(250))


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship(Starships)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    firstname = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(50))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(20), ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(20))
    url = Column(String(250))
    post_id = Column(String(20), ForeignKey('post.id'))
    post = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(20))
    post_id = Column(String(20), ForeignKey('post.id'))
    post = relationship(Post)
    author_id = Column(String(20), ForeignKey('user.id'))
    author = relationship(User)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(20), ForeignKey('user.id'))
    user_from = relationship(User)
    user_to_id = Column(String(20), ForeignKey('user.id'))
    user_to = relationship(User)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
