from mongoengine import EmbeddedDocument, DateField, FloatField, IntField, UUIDField


class AvailabilityEntity(EmbeddedDocument):
    guid = UUIDField(binary=False, required=True, unique=True)
    startDate = DateField(required=True)
    endDate = DateField(required=True)
    availableSeats = IntField(required=True)
    occupiedSeats = IntField(required=True)
    totalPrice = FloatField(required=True)
