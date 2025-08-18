from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual import IndividualTable
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface

class IndividualRepository(IndividualRepositoryInterface):
    def __init__(self, db_connection)-> None:
        self.__db_connection = db_connection

    def insert_individual(
            self, 
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float
        )-> None: 
        with self.__db_connection as database:
            try:
                individual_data = IndividualTable(
                    renda_mensal=renda_mensal,
                    idade=idade,

                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(individual_data)
                database.session.commit(individual_data)
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_individuals(self):
        with self.__db_connection as database:
            try:
                individuals = database.session.query(IndividualTable).all()
                return individuals
            except NoResultFound:
                return []

    def withdraw(self, individual_id: int, amount: float)-> float:
        with self.__db_connection as database:
            try:
                individual = (
                     database.session
                    .query(IndividualTable)
                    .filter(IndividualTable.id == individual_id)
                    .first()
                )
                individual.saldo -= amount                                                                                                                   
                database.session.commit()
                return individual.saldo
            except Exception as exception:
                database.session.roollback()
                raise exception
