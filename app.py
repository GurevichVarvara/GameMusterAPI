from conf import app

from models import Platform


@app.route('/')
def index():
    print(Platform.query.order_by(Platform.id).all())


if __name__ == '__main__':
    app.run()