from base_resources import BaseResource, BaseSequenceResource
from config import app, api
from models import Platform, Genre, Game, User
from serializers import PlatformSerializer, GenreSerializer, GameSerializer, UserSerializer


class Platforms(BaseSequenceResource):
    def __init__(self):
        super().__init__(Platform, PlatformSerializer())


class SinglePlatform(BaseResource):
    def __init__(self):
        super().__init__(Platform, PlatformSerializer())


class Genres(BaseSequenceResource):
    def __init__(self):
        super().__init__(Genre, GenreSerializer())


class SingleGenre(BaseResource):
    def __init__(self):
        super().__init__(Genre, GenreSerializer())


class Games(BaseSequenceResource):
    def __init__(self):
        super().__init__(Game, GameSerializer())


class SingleGame(BaseResource):
    def __init__(self):
        super().__init__(Game, GameSerializer())


class Users(BaseSequenceResource):
    def __init__(self):
        super().__init__(User, UserSerializer())


api.add_resource(Platforms, '/api/platforms')
api.add_resource(SinglePlatform, '/api/platforms/<string:object_id>')
api.add_resource(Genres, '/api/genres')
api.add_resource(SingleGenre, '/api/genres/<string:object_id>')
api.add_resource(Games, '/api/games')
api.add_resource(SingleGame, '/api/games/<string:object_id>')
api.add_resource(Users, '/api/users')


if __name__ == '__main__':
    app.run()
