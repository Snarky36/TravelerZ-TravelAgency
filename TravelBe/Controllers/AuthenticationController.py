from mongoengine import DoesNotExist
from datetime import datetime, timedelta
from Services.UserService import UserService
from Services.SecurityService import SecurityService
from flask import Blueprint, request, jsonify
from flask_httpauth import HTTPTokenAuth
import jwt
from functools import wraps

userService = UserService()
securityService = SecurityService()

authenticationController = Blueprint('authentication_controller', __name__)

auth = HTTPTokenAuth(scheme="Bearer")

@authenticationController.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    if data:
        data['password'] = securityService.encodePassword(data['password'])
        data['role'] = "client"
        user_data = userService.insert_user(data)
        jwt_token = createJwt(user_data)

        if jwt_token:
            return jsonify({"token": jwt_token,
                            "message": "User registered successfully"}), 200
        else:
            return {'error': 'Failed to register user'}, 500
    else:
        return {'error': 'No data provided'}, 400


@authenticationController.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data:
        try:
            user_data = userService.get_userByEmail(data['email'])
            print(user_data)
            if securityService.verifyUser(user_data,data):
                jwt_token = createJwt(user_data)

                return jsonify({"token": jwt_token}), 200
            else:
                return jsonify({'error': 'Email or password are incorrect!'}), 404
        except DoesNotExist:
            return jsonify({'error': 'Email or password are incorrect!'}), 404

@auth.verify_token
def verify_token(jwt_token):
    if not jwt_token:
        return False
    try:
        decoded_jwt = jwt.decode(jwt_token, securityService.getSecurityKey(), algorithms=["HS256"])
        expiration_datetime = datetime.strptime(decoded_jwt["expiration"], "%Y-%m-%d %H:%M:%S.%f")
        if expiration_datetime < datetime.utcnow():
            return False
        return True
    except Exception as e:
        return False

def createJwt(user_data):
    return jwt.encode({
        "role": user_data['role'],
        "email": user_data['email'],
        "guid": str(user_data["user_guid"]),
        "expiration": str(datetime.utcnow().__add__(timedelta(hours=2)))
    }, securityService.getSecurityKey(), algorithm="HS256")