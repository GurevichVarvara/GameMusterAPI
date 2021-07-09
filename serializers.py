from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Platform, Genre


class PlatformSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Platform
        load_instance = True


class GenreSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
