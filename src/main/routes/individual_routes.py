from flask import Blueprint, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.individual_insert_composer import individual_insert_composer
from src.main.composer.individual_lister_composer import individual_lister_composer
from src.main.composer.individual_withdraw_composer import individual_withdraw_composer
from src.main.helpers.handle_controller import handle_controller

individual_route_bp = Blueprint("individual_routes", __name__)

@individual_route_bp.route("/individual", methods=["POST"])
def insert_individual():
    http_request = HttpRequest(body=request.json)
    view = individual_insert_composer()
    return handle_controller(view, http_request)

@individual_route_bp.route("/individual", methods=["GET"])
def list_individual():
    http_request = HttpRequest()
    view = individual_lister_composer()
    return handle_controller(view, http_request)

@individual_route_bp.route("/individual/withdraw/<individual_id>", methods=["PATCH"])
def withdraw_individual(individual_id):
    http_request = HttpRequest(body=request.json, param={ "individual_id": individual_id })
    view = individual_withdraw_composer()
    return handle_controller(view, http_request)
