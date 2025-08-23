from src.controllers.interfaces.individual_withdraw_controller import IndividualWithdrawControllerInterface #pylint: disable=C0301
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class IndividualWithdrawView(ViewInterface):
    def __init__(self, controller: IndividualWithdrawControllerInterface)-> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        individual_id = http_request.param["individual_id"]
        amount = http_request.body.get("amount")
        body_response = self.__controller.withdraw(individual_id, amount)

        return HttpResponse(status_code=204, body=body_response)
