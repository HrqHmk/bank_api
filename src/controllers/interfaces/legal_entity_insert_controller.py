from abc import ABC, abstractmethod

class LegalEntityInsertControllerInterface(ABC):
    @abstractmethod
    def insert(self, legal_entity_info:dict)-> dict:
        pass
