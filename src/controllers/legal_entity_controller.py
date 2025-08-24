import re
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.errors.errors_type.http_bad_request import HttpBadRequestError
from .interfaces.legal_entity_insert_controller import LegalEntityInsertControllerInterface

class LegalEntityInsertController(LegalEntityInsertControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepository)-> None:
        self.__legal_entity_repository = legal_entity_repository
    
    def insert(self, legal_entity_info: dict)-> dict:
        faturamento =  legal_entity_info["faturamento"]
        idade = legal_entity_info["idade"]
        nome_fantasia = legal_entity_info["nome_fantasia"]
        celular = legal_entity_info["celular"]
        email_corporativo = legal_entity_info["email_corporativo"]
        categoria = legal_entity_info["categoria"]
        saldo = legal_entity_info["saldo"]

        self.__validate_nome_fantasia(nome_fantasia)
        self.__validate_faturamento(faturamento)
        self.__insert_legal_entity(
            faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo
        )
        formatted_response = self.__format_response(legal_entity_info)
        return formatted_response

    def __validate_nome_fantasia(self, nome_fantasia: str)-> None:
        #expressao regular para caracteres especiais e espaço em branco
        non_valid_caracters = re.compile(r'[^a-zA-Z\s]')

        if non_valid_caracters.search(nome_fantasia):
            raise HttpBadRequestError("Nome fantasia inválido...")

    def __validate_faturamento(self, faturamento: float)-> None:
        if faturamento < 0 or faturamento == 0:
            raise HttpBadRequestError("Faturamento inválido")
    
    def __insert_legal_entity(
            self,
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float
    )-> None:
        self.__legal_entity_repository.insert_legal_entity(
            faturamento,
            idade,
            nome_fantasia,
            celular,
            email_corporativo,
            categoria,
            saldo
        )

    def __format_response(self, legal_entity_info: dict)-> dict:
        return {
            "data": {
                "type": "Legal Entity",
                "count": 1,
                "attributes": legal_entity_info
            }
        }
