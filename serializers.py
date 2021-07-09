from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Platform


class PlatformSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Platform
        load_instance = True
