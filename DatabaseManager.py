from pymongo import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect


class DatabaseManager:
    def __init__(self):
        self.client = None
        self.uri = "mongodb+srv://root:toor@cluster0.oqzfcbp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    def connect(self):
        try:
            self.client = MongoClient(self.uri, server_api=ServerApi('1'))
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return self.client
        except Exception as e:
            print(e)
            return None

    def getClient(self):
        return self.client

    def connectMongoEngine(self, db_name):
        try:
            # Connect to the MongoDB database using MongoEngine
            connect(db_name, host=self.uri)
            print("Connected to MongoDB database:", db_name)
            return True
        except Exception as e:
            print("Failed to connect to MongoDB database:", e)
            return False


#mongodb+srv://root:<password>@cluster0.oqzfcbp.mongodb.net/