from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_withdraw_controller import LegalEntityWithdrawController

class MockLegalEntityRepository():
    def withdraw(self, legal_entity_id: int, amount: float):
        return 200.00 - amount

    def get_legal_entity_by_id(self, individual_id: int):
        if individual_id == 4:
            return LegalEntityTable(
                faturamento=200.00,
                nome_fantasia="Jhon Doe SA",
                idade=30,
                celular="999999999", 
                email_corporativo="jhondoesa@mail.com",
                categoria="category test",
                saldo=300.00,
                id=4
            )
        return None

def test_withdraw():
    controller = LegalEntityWithdrawController(MockLegalEntityRepository())
    response = controller.withdraw(4, 100)

    assert response["data"]["type"] == "Saldo"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["balance"] == 100
