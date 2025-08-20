from typing import Optional
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.models.sqlite.entities.individual import IndividualTable
from .interfaces.individual_withdraw_controller import IndividualWithdrawControllerInterface

class IndividualWithdrawController(IndividualWithdrawControllerInterface):
    def __init__(self, individual_repository: IndividualRepository)-> None:
        self.__individual_repository = individual_repository

    def withdraw(self, individual_id, amount)-> dict:
        self.__individual_exists(individual_id)
        balance = self.__withdraw_in_db(individual_id, amount)
        response = self.__format_response(balance)
        return response

    def __individual_exists(self, individual_id)->None:
        response: Optional[IndividualTable] = self.__individual_repository.get_individual_by_id(individual_id) # pylint: disable=C0301
        if response is None:
            raise Exception("Usuário não cadastrado")

    def __withdraw_in_db(self, individual_id, amount)->float:
        amount = self.__individual_repository.withdraw(individual_id, amount)
        return amount

    def __format_response(self, balance: float)-> dict:
        return {
            "data": {
                "type": "Saldo",
                "count": 1,
                "attributes": {
                    "balance": balance,
                }
            }
        }
