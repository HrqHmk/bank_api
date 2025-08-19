from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_repository import LegalEntityRepository

class MockConnection:
    def __init__(self)-> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(LegalEntityTable)],
                    [
                        LegalEntityTable(
                            faturamento=200.00, 
                            idade=30,
                            nome_fantasia="Jhon Doe SA", 
                            celular="999999999", 
                            email_corporativo="jhondoesa@mail.com",
                            categoria="category test",
                            saldo=300.00

                        )
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_insert_legal_entity():
    mock_connection = MockConnection()
    repository = LegalEntityRepository(mock_connection)
    repository.insert_legal_entity(
        200.00, 30, "Jhon Doe", "999999999", 
        "jhondoe@mail.com", "category test", 200.00
    )

    mock_connection.session.add.assert_called_once()

def test_list_legal_entity():
    mock_connection = MockConnection()
    repository = LegalEntityRepository(mock_connection)
    response = repository.list_legal_entity()

    mock_connection.session.query.assert_called_once_with(LegalEntityTable)
    assert response[0].nome_fantasia == "Jhon Doe SA"

def test_withdraw():
    mock_connection = MockConnection()
    repository = LegalEntityRepository(mock_connection)
    response = repository.withdraw(1, 200.0)

    mock_connection.session.query.assert_called_once_with(LegalEntityTable)
    mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
    assert response == 100.0

def test_get_individual_by_id():
    mock_connection = MockConnection()
    repository = LegalEntityRepository(mock_connection)
    response = repository.get_legal_entity_by_id(1)
    mock_connection.session.query.assert_called_once_with(LegalEntityTable)
    mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
    assert response.nome_fantasia == "Jhon Doe SA"
