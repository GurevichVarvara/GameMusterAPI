from config import db


class Platform(db.Model):
    __tablename__ = 'gameMuster_platform'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Genre(db.Model):
    __tablename__ = 'gameMuster_genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Game(db.Model):
    __tablename__ = 'gameMuster_game'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
