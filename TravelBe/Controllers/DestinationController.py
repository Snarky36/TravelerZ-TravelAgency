from datetime import datetime

from mongoengine import DoesNotExist
from Entities.AvailabilityEntity import AvailabilityEntity
from Entities.DestinationEntity import DestinationEntity
from flask import Blueprint, request, jsonify, json
from Controllers.AuthenticationController import auth
from uuid import uuid4
from Services.DestinationService import DestinationService

destinationService = DestinationService()


destinationController = Blueprint('destination_controller', __name__)


@destinationController.route("/api/add-destination", methods=["POST"])

def add_destination():
    try:
        data = request.get_json()
        print(data)
        if data:
            destination = destinationService.insert_destination(data)

            print("Destination with availabilities inserted successfully.")
            return jsonify({'message': 'Destination added successfully',
                            "destination": destination}), 200
    except Exception as e:
        return {'error': 'Failed to insert destination'}, 500

@destinationController.route("/api/update-destination/<string:guid>", methods=["PUT"])
def update_destination(guid):
    try:
        data = request.get_json()
        if data:
            destination = destinationService.update_destination(guid, data)

            print("Destination with availabilities inserted successfully.")
            return jsonify({'message': 'Destination added successfully',
                            "destination": destination}), 200
    except Exception as e:
        return {'error': 'Failed to update destination'}, 500

@destinationController.route("/api/delete-destination/<string:guid>", methods=["DELETE"])
def delete_destionation(guid):
    success = destinationService.delete_destination(guid)
    if success:
        return jsonify({'message': 'Destination deleted successfully'}), 200
    else:
        return {'error': 'Failed to delete destination'}, 500


@destinationController.route("/api/add-availability/<string:getValue>", methods=["POST"])
@auth.login_required
def add_availability(getValue):
    return None

@destinationController.route("/api/destination/<string:getValue>", methods=["GET"])
def get_destination(getValue):
    try:
        destination = destinationService.get_destinationByValue(getValue)
        return jsonify(destination), 200
    except Exception as e:
        return {'error': 'Failed to get destination'}, 500


@destinationController.route("/api/destinations", methods=["GET"])

def get_all_destinations():
    try:
        destinations = destinationService.get_allDestinations()
        return jsonify(destinations), 200
    except Exception as e:
        return {'error': 'Failed to get destination'}, 500
