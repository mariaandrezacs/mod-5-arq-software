from src.models.sqlite.entities.pets import PetsTable

from ..models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_lister_controller import PetListerControllerInterface


class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def lister(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "type": pet.type, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
