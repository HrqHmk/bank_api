from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityRepositoryInterface(ABC):
    @abstractmethod
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
        pass

    @abstractmethod
    def list_legal_entity(self)-> list[LegalEntityTable]:
        pass
