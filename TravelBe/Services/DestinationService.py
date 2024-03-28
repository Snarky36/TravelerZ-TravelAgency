import base64
import io
from datetime import datetime

from flask import jsonify, json
from mongoengine import DoesNotExist

from DatabaseManager import DatabaseManager
from Entities.AvailabilityEntity import AvailabilityEntity
from Entities.DestinationEntity import DestinationEntity
from uuid import uuid4, UUID


class DestinationService:
    def __init__(self):
        self.databaseManager = DatabaseManager()
        self.db = self.databaseManager.connectMongoEngine("travel_db")

    def insert_destination(self, data):
        try:
            data['destination_guid'] = uuid4()
           # binaryDataImage = self.save_image_from_base64(data['image'])

            print("Destination", data)
            destination_data = {
                'destination_guid': data['destination_guid'],
                'name': data['name'],
                'image': data['image'],
                'location': data['location'],
                'description':data['description'],
                'price': data['price'],
                'availableSeats': data['availableSeats'],
                'discountPercent': data['discountPercent']
            }
            availabilities_data = data['availabilities']
            destination_entity = DestinationEntity(**destination_data)

            for availability_data in availabilities_data:
                availability_data['startDate'] = datetime.strptime(availability_data['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
                availability_data['endDate'] = datetime.strptime(availability_data['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
                availability_entity = AvailabilityEntity(**availability_data)
                destination_entity.availabilities.append(availability_entity)

            destination_entity.save()

            return destination_entity.to_json()
        except Exception as e:
            return False, str(e)

    def update_destination(self, destination_guid, data):
        try:
            destination_entity = DestinationEntity.objects.get(destination_guid=destination_guid)

            destination_entity.name = data['name']
            destination_entity.location = data['location']
            destination_entity.price = data['price']
            destination_entity.availableSeats = data['availableSeats']
            destination_entity.discountPercent = data['discountPercent']
            destination_entity.description = data['description']

            destination_entity.availabilities.clear()
            availabilities_data = data['availabilities']
            for availability_data in availabilities_data:
                availability_entity = AvailabilityEntity(**availability_data)
                destination_entity.availabilities.append(availability_entity)

            destination_entity.save()

            return destination_entity.to_json()
        except Exception as e:
            return False, str(e)

    def delete_destination(self, destination_guid):
        try:
            destination_entity = DestinationEntity.objects.get(destination_guid=destination_guid)
            destination_entity.delete()

            return True
        except DoesNotExist:
            return False
        except Exception as e:
            return False, str(e)

    def get_destinationByValue(self, value):
        try:
            destination_guid = UUID(value, version=4)
            return self.get_destinationByGuid(destination_guid)
        except Exception:
            return self.get_destintionByName(value)

    def get_destinationByGuid(self, destination_guid):
        destination = DestinationEntity.objects.get(destination_guid=destination_guid)
        return destination.to_json()

    def get_destintionByName(self, name):
        destination = DestinationEntity.objects.get(name=name)
        return destination.to_json()

    def get_allDestinations(self):
        destinations = DestinationEntity.objects.all()
        destination_data = []
        for destination in destinations:
            destination_data.append(destination.to_json())

        return destination_data