from .pet_delete_controller import PetDeleteController


def test_delete_pet(mocker):
    mocke_repository = mocker.Mock()
    controller = PetDeleteController(mocke_repository)
    controller.delete("amiguinho")

    mocke_repository.delete_pets.assert_called_once_with("amiguinho")
