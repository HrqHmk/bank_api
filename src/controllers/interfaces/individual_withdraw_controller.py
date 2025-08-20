from abc import ABC, abstractmethod

class IndividualWithdrawControllerInterface(ABC):
    @abstractmethod
    def withdraw(self, individual_id:int, amount: float)-> dict:
        pass
