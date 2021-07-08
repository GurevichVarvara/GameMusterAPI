from conf import db


class Platform(db.Model):
    __tablename__ = 'gameMuster_platform'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
