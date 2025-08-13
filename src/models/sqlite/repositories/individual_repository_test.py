from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.individual import IndividualTable
from .individual_repository import IndividualRepository

class MockConnection:
    def __init__(self)-> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(IndividualTable)],
                    [
                        IndividualTable(
                            renda_mensal=200.00, 
                            idade=30,
                            nome_completo="Jhon Doe", 
                            celular="999999999", 
                            email="jhondoe@mail.com",
                            categoria="category test",
                            saldo=200.00

                        )
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_insert_individual():
    mock_connection = MockConnection()
    repository = IndividualRepository(mock_connection)
    repository.insert_individual(
        200.00, 30, "Jhon Doe", "999999999", 
        "jhondoe@mail.com", "category test", 200.00
    )

    mock_connection.session.add.assert_called_once()

def test_list_individuals():
    mock_connection = MockConnection()
    repository = IndividualRepository(mock_connection)
    response = repository.list_individuals()

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    assert response[0].nome_completo == "Jhon Doe"

def test_withdraw():
    mock_connection = MockConnection()
    repository = IndividualRepository(mock_connection)
    repository.withdraw(1, 200.0)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter.assert_called_once_with(IndividualTable.id == 1)
    mock_connection.session.update.assert_called_once()
    mock_connection.session.update.assert_called_once_with({
        IndividualTable.saldo: IndividualTable.saldo - 200.0
    })
