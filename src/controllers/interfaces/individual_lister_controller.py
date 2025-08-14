from abc import ABC, abstractmethod

class IndividualListerControllerInterface(ABC):
    @abstractmethod
    def list(self)-> dict:
        pass
