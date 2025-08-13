from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

class LegalEntityRepository(LegalEntityRepositoryInterface):
    def __init__(self, db_connection)-> None:
        self.__db_connection = db_connection

    def insert_legal_entity(
            self, 
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float
        )-> None: 
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(legal_entity_data)
                database.session.commit(legal_entity_data)
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_legal_entity(self):
        with self.__db_connection as database:
            try:
                legal_entities = database.session.query(LegalEntityTable).all()
                return legal_entities
            except NoResultFound:
                return []

    def withdraw(self, legal_entity_id, amount):
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.id == legal_entity_id)
                    .update({LegalEntityTable.saldo: LegalEntityTable.saldo - amount})
                )
                database.session.commit()
            except Exception as exception:
                database.session.roollback()
                raise exception
