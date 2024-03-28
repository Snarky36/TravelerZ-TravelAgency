from mongoengine import EmbeddedDocument, DateField, FloatField, IntField


class AvailabilityEntity(EmbeddedDocument):
    startDate = DateField(required=True)
    endDate = DateField(required=True)
    availableSeats = IntField(required=True)
    totalPrice = FloatField(required=True)
