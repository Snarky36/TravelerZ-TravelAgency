from flask import jsonify
from mongoengine import DoesNotExist

from DatabaseManager import DatabaseManager
from Entities.UserEntity import UserEntity
from uuid import uuid4, UUID


class UserService:
    def __init__(self):
        self.databaseManager = DatabaseManager()
        self.db = self.databaseManager.connectMongoEngine("travel_db")

    def insert_user(self, user_data):
        user_data['user_guid'] = uuid4()
        print(user_data)
        try:
            user_entity = UserEntity(**user_data)  # Create a UserEntity instance from
            print(user_entity)
            user_entity.save()
            return user_entity
        except Exception as e:
            return False, str(e)

    def get_userbyValue(self, value):
        try:
            user_guid = UUID(value, version=4)
            return self.get_userByGuid(user_guid)
        except Exception:
            return self.get_userByEmail(value)

    def get_userByGuid(self, user_guid):
        user = UserEntity.objects.get(user_guid=user_guid)

        user_data = {
            'name': user.name,
            'email': user.email,
            'user_guid': user.user_guid,
            'password': user.password,
            'role': user.role
        }
        print(user, user_data)
        return user_data

    def get_userByEmail(self, email):
        user = UserEntity.objects.get(email=email)
        user_data = {
            'name': user.name,
            'email': user.email,
            'user_guid': user.user_guid,
            'password': user.password,
            'role': user.role
        }
        print("user", user_data)
        return user_data

    def get_allUsers(self):
        users = UserEntity.objects.all()
        users_data = []
        for user in users:
            user_data = {
                'name': user.name,
                'email': user.email,
                'user_guid': user.user_guid,
                'password': user.password,
                'role': user.role
            }
            users_data.append(user_data)

        return users_data
