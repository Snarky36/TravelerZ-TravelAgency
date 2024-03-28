import base64
import io

from mongoengine import Document, StringField, FloatField, IntField, EmbeddedDocumentListField, UUIDField, BinaryField
from Entities.AvailabilityEntity import AvailabilityEntity


class DestinationEntity(Document):

    destination_guid = UUIDField(binary=False, required=True, unique=True)
    name = StringField(required=True, max_length=100)
    location = StringField(required=True, max_length=100)
    description = StringField(max_length=1000)
    image = StringField()
    price = FloatField(required=True)
    availableSeats = IntField(required=True)
    discountPercent = IntField(max_length=100)
    availabilities = EmbeddedDocumentListField(AvailabilityEntity)

    meta = {
        'collection': 'destinations'
    }

    def to_json(self):
        return {
            'destination_guid': str(self.destination_guid),
            'name': self.name,
            'location': self.location,
            'description': self.description,
            'image': self.image,
            'price': self.price,
            'availableSeats': self.availableSeats,
            'discountPercent': self.discountPercent,
            'availabilities': [
                {
                    'startDate': str(availability.startDate),
                    'endDate': str(availability.endDate),
                    'availableSeats': availability.availableSeats,
                    'totalPrice': availability.totalPrice
                }
                for availability in self.availabilities
            ]
        }