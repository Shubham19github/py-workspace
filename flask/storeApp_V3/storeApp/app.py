from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from items import Item, Items

PORT = 5500

app = Flask(__name__)
app.secret_key = '3ec8eY-$et'

api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<int:_id>', '/item')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
	app.run(port = PORT, debug=True)