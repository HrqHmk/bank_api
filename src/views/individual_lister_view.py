from src.controllers.interfaces.individual_lister_controller import IndividualListerControllerInterface #pylint: disable=C0301
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class IndividualListerView(ViewInterface):
    def __init__(self, controller: IndividualListerControllerInterface)-> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        body_response = self.__controller.list()

        return HttpResponse(status_code=200, body=body_response)
