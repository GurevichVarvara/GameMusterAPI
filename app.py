from flask_restful import Resource

from config import app, api
from models import Platform, Genre, Game
from serializers import PlatformSerializer, GenreSerializer, GameSerializer


class Platforms(Resource):
    def get(self):
        platforms = Platform.query.order_by(Platform.id).all()
        serializer = PlatformSerializer()

        return serializer.dumps(platforms, many=True)


class Genres(Resource):
    def get(self):
        genres = Genre.query.order_by(Genre.id).all()
        serializer = GenreSerializer()

        return serializer.dumps(genres, many=True)


class Games(Resource):
    def get(self):
        games = Game.query.order_by(Game.id).all()
        serializer = GameSerializer()

        return serializer.dumps(games, many=True)


api.add_resource(Platforms, '/api/platforms')
api.add_resource(Genres, '/api/genres')
api.add_resource(Games, '/api/games')


if __name__ == '__main__':
    app.run()
