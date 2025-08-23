from flask import Response, jsonify
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest

def handle_controller(view: ViewInterface, http_request: HttpRequest)-> Response:
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
