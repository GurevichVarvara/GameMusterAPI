from config import app
from models import Platform, Genre
from serializers import PlatformSerializer, GenreSerializer


@app.route('/api/platforms')
def get_platforms():
    platforms = Platform.query.order_by(Platform.id).all()
    serializer = PlatformSerializer()

    return serializer.dumps(platforms, many=True)


@app.route('/api/genres')
def get_genres():
    genres = Genre.query.order_by(Genre.id).all()
    serializer = GenreSerializer()

    return serializer.dumps(genres, many=True)


if __name__ == '__main__':
    app.run()
