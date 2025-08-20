from src.models.sqlite.entities.individual import IndividualTable
from .individual_withdraw_controller import IndividualWithdrawController

class MockIndividualRepository():
    def withdraw(self, individual_id: int, amount: float):
        return 200.00 - amount

    def get_individual_by_id(self, individual_id: int):
        if individual_id == 4:
            return IndividualTable(
                nome_completo="Jhon Doe", 
                idade=30,
                email="jhondoe@mail.com",
                celular="99 99999999",
                categoria="category 1",
                renda_mensal=200.00,
                saldo=200.00,
                id=4
            )
        return None

def test_withdraw():
    controller = IndividualWithdrawController(MockIndividualRepository())
    response = controller.withdraw(4, 100)

    assert response["data"]["type"] == "Saldo"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["balance"] == 100
