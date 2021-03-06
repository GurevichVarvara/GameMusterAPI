from flask import request, abort

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

    def get(self):
        user_id = User.decode_auth_token(request.headers['Authorization'])
        user = User.query.get(user_id)

        if user.is_staff:
            result = super().get()
        else:
            result = self.serializer.dump(user)

        return result


class SingleUser(BaseResource):
    def __init__(self):
        super().__init__(User, UserSerializer())

    @staticmethod
    def _get_user_by_token(token):
        user_id = User.decode_auth_token(token)

        return User.query.get(user_id)

    def get(self, object_id):
        result_user = self._get_user_by_token(request.headers['Authorization'])

        if result_user.id != object_id:
            abort(404)

        return super().get(object_id)


api.add_resource(Platforms, '/api/platforms')
api.add_resource(SinglePlatform, '/api/platforms/<string:object_id>')
api.add_resource(Genres, '/api/genres')
api.add_resource(SingleGenre, '/api/genres/<string:object_id>')
api.add_resource(Games, '/api/games')
api.add_resource(SingleGame, '/api/games/<string:object_id>')
api.add_resource(Users, '/api/users')
api.add_resource(SingleUser, '/api/profile')


if __name__ == '__main__':
    app.run()
