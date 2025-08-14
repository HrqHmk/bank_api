from abc import ABC, abstractmethod

class IndividualInsertControllerInterface(ABC):
    @abstractmethod
    def insert(self, individual_info:dict)-> dict:
        pass
