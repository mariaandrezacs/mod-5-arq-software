from flask import Blueprint, jsonify

from src.main.composer.pet_delete_composer import pet_delete_composer
from src.main.composer.pet_lister_composer import pet_lister_composer

from ...errors.error_handler import handle_errors
from ...views.http_types.http_request import HttpRequest

pet_route_bp = Blueprint("pets_routes", __name__)


@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@pet_route_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    try:
        http_request = HttpRequest(param={"name": name})
        view = pet_delete_composer()
        http_reponse = view.handle(http_request)

        return jsonify(http_reponse.body), http_reponse.status_code

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_reponse.body), http_response.status_code
