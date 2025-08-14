from src.models.sqlite.entities.individual import IndividualTable
from .individual_lister_controller import IndividualListerController

class MockPetsRepository:
    def list_individuals(self):
        return [
            IndividualTable(
                nome_completo="Jhon Doe", 
                idade=30,
                email="jhondoe@mail.com",
                celular="99 99999999",
                categoria="category 1",
                renda_mensal=200.00,
                saldo=200.00 ,
                id=4
            ),
            IndividualTable(
                nome_completo="Jhon Doe 2", 
                idade=31,
                email="jhondoe2@mail.com",
                celular="99 99999999",
                categoria="category 2",
                renda_mensal=300.00,
                saldo=300.00 ,
                id=6
            ),
        ]

def test_list_individuals():
    controller = IndividualListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data":{
            "type": "Individuals",
            "count": 2,
            "attributes": [
                { 
                    "nome": "Jhon Doe", 
                    "email": "jhondoe@mail.com",
                    "celular": "99 99999999",
                    "categoria": "category 1",
                    "id": 4
                },
                { 
                    "nome": "Jhon Doe 2", 
                    "email": "jhondoe2@mail.com",
                    "celular": "99 99999999",
                    "categoria": "category 2",
                    "id": 6
                },
            ]
        }
    }

    assert response == expected_response
