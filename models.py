import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "CastingAgency"
database_path = "postgres://guzemgdwldzpsm:43d9f428fb3828c1c1f1cbb37b5745250a1a157c462ffb425b486880b35698f9@ec2-50-16-198-4.compute-1.amazonaws.com:5432/ddfdg9qoer2t53"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Extend the base Model class to add common methods
'''


class commonMethods(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


'''
Movie
'''


class Movie(commonMethods):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime)
    actors = db.relationship('Actor', backref='movie', lazy=True)

    def __init__(self, title, release):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


'''
Actor
'''


class Actor(commonMethods):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'),
                         nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie.id
        }
