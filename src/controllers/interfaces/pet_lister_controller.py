from abc import ABC, abstractmethod


class PetListerControllerInterface(ABC):
    @abstractmethod
    def lister(self) -> dict:
        pass
