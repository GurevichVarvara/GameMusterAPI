from flask_restful import Resource


class BaseSequenceResource(Resource):
    def __init__(self, class_name, serializer):
        self.class_name = class_name
        self.serializer = serializer

    def get(self):
        sequence = self.class_name.query.order_by(self.class_name.id).all()

        return self.serializer.dumps(sequence, many=True)


class BaseResource(Resource):
    def __init__(self, class_name, serializer):
        self.class_name = class_name
        self.serializer = serializer

    def get(self, object_id):
        target = self.class_name.query.get(object_id)

        return self.serializer.dump(target)