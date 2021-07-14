import os
import datetime

import jwt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from config import db

game_platforms = db.Table(
    'gameMuster_game_platforms',
    db.Column('game_id', db.Integer, db.ForeignKey('gameMuster_game.id'), primary_key=True),
    db.Column('platform_id', db.Integer, db.ForeignKey('gameMuster_platform.id'), primary_key=True)
)

game_genres = db.Table(
    'gameMuster_game_genres',
    db.Column('game_id', db.Integer, db.ForeignKey('gameMuster_game.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('gameMuster_genre.id'), primary_key=True)
)


class Platform(db.Model):
    __tablename__ = 'gameMuster_platform'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)


class Genre(db.Model):
    __tablename__ = 'gameMuster_genre'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)


class Screenshot(db.Model):
    __tablename__ = 'gameMuster_screenshot'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img_url = db.Column(db.String, nullable=False)
    game_id = db.Column(db.Integer, ForeignKey('gameMuster_game.id'), nullable=False)


class Game(db.Model):
    __tablename__ = 'gameMuster_game'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    screenshots = relationship('Screenshot')
    genres = db.relationship('Genre', secondary=game_genres, lazy='subquery',
                             backref=db.backref('gameMuster_game', lazy=True))
    platforms = db.relationship('Platform', secondary=game_platforms, lazy='subquery',
                                backref=db.backref('gameMuster_game', lazy=True))


class User(db.Model):
    __tablename__ = 'users_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_staff = db.Column(db.Boolean)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    birthday = db.Column(db.Date)
    active_time = db.Column(db.DateTime, default=datetime.datetime.now())
    unconfirmed_email = db.Column(db.String)

    @staticmethod
    def encode_jwt_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }

            return jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

