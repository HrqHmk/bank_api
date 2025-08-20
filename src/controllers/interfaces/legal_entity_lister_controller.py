from abc import ABC, abstractmethod

class LegalEntityListerControllerInterface(ABC):
    @abstractmethod
    def list(self)-> dict:
        pass
