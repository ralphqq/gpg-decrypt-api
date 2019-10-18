from flask_restful import Api

from app.resource.decrypt import DecryptMessage

api = Api()
api.add_resource(DecryptMessage, '/')