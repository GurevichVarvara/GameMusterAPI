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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Genre(db.Model):
    __tablename__ = 'gameMuster_genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Screenshot(db.Model):
    __tablename__ = 'gameMuster_screenshot'

    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String)
    game_id = db.Column(db.Integer, ForeignKey('gameMuster_game.id'))


class Game(db.Model):
    __tablename__ = 'gameMuster_game'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    screenshots = relationship('Screenshot')
    genres = db.relationship('Genre', secondary=game_genres, lazy='subquery',
                             backref=db.backref('gameMuster_game', lazy=True))
    platforms = db.relationship('Platform', secondary=game_platforms, lazy='subquery',
                                backref=db.backref('gameMuster_game', lazy=True))
