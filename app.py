from config import app
from models import Platform
from serializers import PlatformSerializer


@app.route('/api/platforms')
def get_platforms():
    platforms = Platform.query.order_by(Platform.id).all()
    serializer = PlatformSerializer()

    return serializer.dumps(platforms, many=True)


if __name__ == '__main__':
    app.run()