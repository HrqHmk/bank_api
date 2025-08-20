from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_lister_controller import LegalEntityListerController

class MockLegalEntityRepository:
    def list_legal_entity(self):
        return [
            LegalEntityTable(
                nome_fantasia="Jhon Doe SA", 
                idade=30,
                email_corporativo="jhondoe@mail.com",
                celular="99 99999999",
                categoria="category 1",
                faturamento=200.00,
                saldo=200.00 ,
                id=4
            ),
            LegalEntityTable(
                nome_fantasia="Jhon Doe SA 2", 
                idade=31,
                email_corporativo="jhondoe2@mail.com",
                celular="99 99999999",
                categoria="category 2",
                faturamento=300.00,
                saldo=300.00 ,
                id=6
            ),
        ]

def test_list_legal_entities():
    controller = LegalEntityListerController(MockLegalEntityRepository())
    response = controller.list()

    expected_response = {
        "data":{
            "type": "Legal Entities",
            "count": 2,
            "attributes": [
                { 
                    "nome": "Jhon Doe SA", 
                    "email": "jhondoe@mail.com",
                    "celular": "99 99999999",
                    "categoria": "category 1",
                    "id": 4
                },
                { 
                    "nome": "Jhon Doe SA 2", 
                    "email": "jhondoe2@mail.com",
                    "celular": "99 99999999",
                    "categoria": "category 2",
                    "id": 6
                },
            ]
        }
    }

    assert response == expected_response
