from mongoengine import DoesNotExist
from Services.UserService import UserService
from Services.SecurityService import SecurityService
from flask import Blueprint, request, jsonify
from Controllers.AuthenticationController import auth

userService = UserService()
securityService = SecurityService()

userController = Blueprint('user_controller', __name__)


@userController.route("/api/add-user", methods=["POST"])
@auth.login_required
def post():
    data = request.get_json()
    print(data)
    if data:
        data['password'] = securityService.encodePassword(data['password'])
        user_id = userService.insert_user(data)
        if user_id:
            return {'message': 'User inserted successfully', 'user_id': user_id}, 201
        else:
            return {'error': 'Failed to insert user'}, 500
    else:
        return {'error': 'No data provided'}, 400


@userController.route("/api/user/<string:getValue>", methods=["GET"])
@auth.login_required
def get(getValue):
    try:
        user = userService.get_userbyValue(getValue)
        return jsonify(user), 200
    except DoesNotExist:
        return jsonify({'error': 'No user found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@userController.route("/api/users", methods=["GET"])
@auth.login_required
def get_all_users():
    try:
        users_data = userService.get_allUsers()
        return jsonify(users_data), 200
    except DoesNotExist:
        return jsonify({'error': 'No users found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
