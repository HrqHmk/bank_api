import pytest
from .individual_insert_controller import IndividualInsertController

class MockIndividualRepository():
    def insert_individual(
            self,
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float
    ):
        pass

def test_individual_insert():
    individual_info= {
        "renda_mensal":200.00,
        "idade":30,
        "nome_completo":"Jhon Doe",
        "celular":"99 99999999",
        "email":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.00
    }

    controller = IndividualInsertController(MockIndividualRepository())
    response = controller.insert(individual_info)

    assert response["data"]["type"] == "Individual"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == individual_info

def test_insert_error_name():
    individual_info= {
        "renda_mensal":200.00,
        "idade":30,
        "nome_completo":"Jhon D@e",
        "celular":"99 99999999",
        "email":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.00
    }

    controller = IndividualInsertController(MockIndividualRepository())
    with pytest.raises(Exception):
        controller.insert(individual_info)

def test_insert_invalid_renda_mensal():
    individual_info= {
        "renda_mensal":0,
        "idade":30,
        "nome_completo":"Jhon Doe",
        "celular":"99 99999999",
        "email":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.0
    }

    controller = IndividualInsertController(MockIndividualRepository())
    with pytest.raises(Exception):
        controller.insert(individual_info)
