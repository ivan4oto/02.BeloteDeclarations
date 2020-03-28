import json


class Jsonable:
    def to_json(self):
        return json.dumps(self, cls=OurEncoder)


class OurEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__json__"):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)
