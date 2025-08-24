from typing import Optional
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.errors.errors_type.http_not_found import HttpNotFoundError
from .interfaces.legal_entity_withdraw_controller import LegalEntityWithdrawControllerInterface

class LegalEntityWithdrawController(LegalEntityWithdrawControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepository)-> None:
        self.__legal_entity_repository = legal_entity_repository

    def withdraw(self, legal_entity_id, amount)-> dict:
        self.__legal_entity_exists(legal_entity_id)
        balance = self.__withdraw_in_db(legal_entity_id, amount)
        response = self.__format_response(balance)
        return response

    def __legal_entity_exists(self, legal_entity_id)->None:
        response: Optional[LegalEntityTable] = self.__legal_entity_repository.get_legal_entity_by_id(legal_entity_id) # pylint: disable=C0301
        if response is None:
            raise HttpNotFoundError("Entidade não cadastrada")

    def __withdraw_in_db(self, legal_entity_id, amount)->float:
        amount = self.__legal_entity_repository.withdraw(legal_entity_id, amount)
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
