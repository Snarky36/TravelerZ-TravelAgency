from mongoengine import Document, StringField, UUIDField


class UserEntity(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True, max_length=100, unique=True)
    user_guid = UUIDField(binary=False, required=True, unique=True)
    password = StringField(required=True, max_length=100)
    role = StringField(required=True, max_length=100)

    meta = {
        'collection': 'users'
    }
