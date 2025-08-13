from abc import ABC, abstractmethod
from src.models.sqlite.entities.individual import IndividualTable

class IndividualRepositoryInterface(ABC):
    @abstractmethod
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
        pass

    @abstractmethod
    def list_individuals(self)-> list[IndividualTable]:
        pass
    
    @abstractmethod
    def withdraw(self, individual_id: int, amount: float)-> None:
        pass
