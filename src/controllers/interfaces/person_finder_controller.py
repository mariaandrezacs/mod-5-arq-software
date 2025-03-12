from abc import ABC, abstractmethod


class PersonCreatorControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> dict:
        pass
