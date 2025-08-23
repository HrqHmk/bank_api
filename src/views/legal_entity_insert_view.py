from src.controllers.interfaces.legal_entity_insert_controller import LegalEntityInsertControllerInterface #pylint: disable=C0301
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityInsertView(ViewInterface):
    def __init__(self, controller: LegalEntityInsertControllerInterface)-> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        legal_entity_info = http_request.body
        body_response = self.__controller.insert(legal_entity_info)

        return HttpResponse(status_code=201, body=body_response)
