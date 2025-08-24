from src.controllers.interfaces.individual_insert_controller import IndividualInsertControllerInterface #pylint: disable=C0301
from src.validators.individual_insert_validator import individual_insert_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class IndividualInsertView(ViewInterface):
    def __init__(self, controller: IndividualInsertControllerInterface)-> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        individual_insert_validator(http_request)
        individual_info = http_request.body
        body_response = self.__controller.insert(individual_info)

        return HttpResponse(status_code=201, body=body_response)
