from abc import ABC, abstractmethod

class LegalEntityWithdrawControllerInterface(ABC):
    @abstractmethod
    def withdraw(self, legal_entity_id:int, amount: float)-> dict:
        pass
