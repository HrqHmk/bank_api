import re
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.errors.errors_type.http_bad_request import HttpBadRequestError
from .interfaces.individual_insert_controller import IndividualInsertControllerInterface

class IndividualInsertController(IndividualInsertControllerInterface):
    def __init__(self, individual_repository: IndividualRepository)-> None:
        self.__individual_repository = individual_repository
    
    def insert(self, individual_info: dict)-> dict:
        renda_mensal =  individual_info["renda_mensal"]
        idade = individual_info["idade"]
        nome_completo = individual_info["nome_completo"]
        celular = individual_info["celular"]
        email = individual_info["email"]
        categoria = individual_info["categoria"]
        saldo = individual_info["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__validate_renda_mensal(renda_mensal)
        self.__insert_individual(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )
        formatted_response = self.__format_response(individual_info)
        return formatted_response

    def __validate_nome_completo(self, nome_completo: str)-> None:
        #expressao regular para caracteres especiais e espaço em branco
        non_valid_caracters = re.compile(r'[^a-zA-Z\s]')

        if non_valid_caracters.search(nome_completo):
            raise HttpBadRequestError("Nome da pessoa inválido...")

    def __validate_renda_mensal(self, renda_mensal: float)-> None:
        if renda_mensal < 0 or renda_mensal == 0:
            raise HttpBadRequestError("Renda Mensal inválida")
    
    def __insert_individual(
            self,
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float
    )-> None:
        self.__individual_repository.insert_individual(
            renda_mensal,
            idade,
            nome_completo,
            celular,
            email,
            categoria,
            saldo
        )

    def __format_response(self, individual_info: dict)-> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 1,
                "attributes": individual_info
            }
        }
