from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Platform, Genre, Game, Screenshot, User


class PlatformSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Platform
        load_instance = True


class GenreSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True


class ScreenshotSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Screenshot
        load_instance = True


class GameSerializer(SQLAlchemyAutoSchema):
    screenshots = fields.Nested(ScreenshotSerializer, many=True)
    platforms = fields.Nested(PlatformSerializer, many=True)
    genres = fields.Nested(GenreSerializer, many=True)

    class Meta:
        model = Game
        load_instance = True


class UserSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True