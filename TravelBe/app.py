
from flask import Flask
from pymongo import MongoClient
from Controllers.UserController import userController
from Controllers.AuthenticationController import authenticationController
from Controllers.DestinationController import destinationController
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(userController)
app.register_blueprint(authenticationController)
app.register_blueprint(destinationController)
client = MongoClient('localhost', 27017)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)