from flask import Blueprint, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.legal_entity_insert_composer import legal_entity_insert_composer
from src.main.composer.legal_entity_lister_composer import legal_entity_lister_composer
from src.main.composer.legal_entity_withdraw_composer import legal_entity_withdraw_composer
from src.main.helpers.handle_controller import handle_controller

legal_entity_route_bp = Blueprint("legal_entity_routes", __name__)

@legal_entity_route_bp.route("/legal_entity", methods=["POST"])
def insert_legal_entity():
    http_request = HttpRequest(body=request.json)
    view = legal_entity_insert_composer()
    return handle_controller(view, http_request)

@legal_entity_route_bp.route("/legal_entity", methods=["GET"])
def list_legal_entity():
    http_request = HttpRequest()
    view = legal_entity_lister_composer()
    return handle_controller(view, http_request)

@legal_entity_route_bp.route("/legal_entity/withdraw/<legal_entity_id>", methods=["PATCH"])
def withdraw_legal_entity(legal_entity_id):
    http_request = HttpRequest(body=request.json, param={ "legal_entity_id": legal_entity_id })
    view = legal_entity_withdraw_composer()
    return handle_controller(view, http_request)
