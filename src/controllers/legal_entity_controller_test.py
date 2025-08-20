import pytest
from .legal_entity_controller import LegalEntityInsertController

class MockLegalEntityRepository():
    def insert_legal_entity(
            self,
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float
    ):
        pass

def test_legal_entity_insert():
    legal_entity_info= {
        "faturamento":200.00,
        "idade":30,
        "nome_fantasia":"Jhon Doe SA",
        "celular":"99 99999999",
        "email_corporativo":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.00
    }

    controller = LegalEntityInsertController(MockLegalEntityRepository())
    response = controller.insert(legal_entity_info)

    assert response["data"]["type"] == "Legal Entity"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == legal_entity_info

def test_insert_error_name():
    legal_entity_info= {
        "faturamento":200.00,
        "idade":30,
        "nome_fantasia":"Jhon D@e",
        "celular":"99 99999999",
        "email_corporativo":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.00
    }

    controller = LegalEntityInsertController(MockLegalEntityRepository())
    with pytest.raises(Exception):
        controller.insert(legal_entity_info)

def test_insert_invalid_renda_mensal():
    legal_entity_info= {
        "faturamento":200.00,
        "idade":30,
        "nome_fantasia":"Jhon D@e",
        "celular":"99 99999999",
        "email_corporativo":"jhondoe@mail.com",
        "categoria":"category 1",
        "saldo":200.00
    }

    controller = LegalEntityInsertController(MockLegalEntityRepository())
    with pytest.raises(Exception):
        controller.insert(legal_entity_info)
