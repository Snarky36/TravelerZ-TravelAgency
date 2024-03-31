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
@auth.login_required
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
@auth.login_required
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
@auth.login_required
def delete_destionation(guid):
    success = destinationService.delete_destination(guid)
    if success:
        return jsonify({'message': 'Destination deleted successfully'}), 200
    else:
        return {'error': 'Failed to delete destination'}, 500


@destinationController.route("/api/add-reservation/<string:guid>", methods=["POST"])
@auth.login_required
def add_availability(guid):
    try:
        data = request.get_json()
        print(data)
        if data:
            destination = destinationService.add_reservation(guid, data)

            print("Destination with availabilities inserted successfully.")
            return jsonify({'message': 'Destination added successfully',
                            "destination": destination}), 200
    except Exception as e:
        return {'error': 'Failed to insert destination'}, 500

@destinationController.route("/api/reserve-place/<string:guid>/<string:reservedGuid>", methods=["GET"])
@auth.login_required
def reserve_place(guid, reservedGuid):
    try:
        destination = destinationService.reserve_place(guid, reservedGuid)

        print("Destination with availabilities inserted successfully.")
        return jsonify({'message': 'Destination added successfully',
                            "destination": destination}), 200
    except Exception as e:
        return {'error': 'Failed to insert destination'}, 500

@destinationController.route("/api/update-reservation/<string:guid>/<string:reserveGuid>", methods=["PUT"])
@auth.login_required
def update_reservation(guid, reserveGuid):
    try:
        data = request.get_json()
        print(data)
        if data:
            destination = destinationService.update_reservation(guid, reserveGuid, data)

            print("Destination with availabilities inserted successfully.")
            return jsonify({'message': 'Destination added successfully',
                            "destination": destination}), 200
    except Exception as e:
        return {'error': 'Failed to insert destination'}, 500

@destinationController.route("/api/delete-reservation/<string:dest_guid>/<string:reserveGuid>", methods=["DELETE"])
@auth.login_required
def delete_availability(dest_guid, reserveGuid):
    success = destinationService.delete_reservation(dest_guid, reserveGuid);
    if success:
        return jsonify({'message': 'Destination deleted successfully'}), 200
    else:
        return {'error': 'Failed to delete destination'}, 500

@destinationController.route("/api/destination/<string:getValue>", methods=["GET"])
@auth.login_required
def get_destination(getValue):
    try:
        destination = destinationService.get_destinationByValue(getValue)
        return jsonify(destination), 200
    except Exception as e:
        return {'error': 'Failed to get destination'}, 500


@destinationController.route("/api/destinations", methods=["GET"])
@auth.login_required
def get_all_destinations():
    try:
        destinations = destinationService.get_allDestinations()
        return jsonify(destinations), 200
    except Exception as e:
        return {'error': 'Failed to get destination'}, 500
