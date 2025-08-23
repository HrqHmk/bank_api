from src.controllers.interfaces.legal_entity_withdraw_controller import LegalEntityWithdrawControllerInterface #pylint: disable=C0301
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityWithdrawView(ViewInterface):
    def __init__(self, controller: LegalEntityWithdrawControllerInterface)-> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        legal_entity_id = http_request.param["legal_entity_id"]
        amount = http_request.body.get("amount")
        body_response = self.__controller.withdraw(legal_entity_id, amount)

        return HttpResponse(status_code=204, body=body_response)
