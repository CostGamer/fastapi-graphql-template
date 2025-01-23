from typing import Protocol

from app.models import Pet


class PetRepositoryProtocol(Protocol):
    async def create_pet(self, name: str, breed: str, age: int, owner_id: int) -> Pet:
        """
        Creates a new pet in the database.

        Args:
            name (str): The name of the pet.
            breed (str): The breed of the pet.
            age (int): The age of the pet.
            owner_id (int): The ID of the owner.

        Returns:
            Pet: The created pet object.
        """
        pass

    async def get_pet_by_id(self, pet_id: int) -> Pet | None:
        """
        Retrieves a pet by its ID.

        Args:
            pet_id (int): The ID of the pet.

        Returns:
            Optional[Pet]: The pet object if found, otherwise None.
        """
        pass

    async def get_pets_by_owner(self, owner_id: int) -> list[Pet]:
        """
        Retrieves all pets belonging to a specific owner.

        Args:
            owner_id (int): The ID of the owner.

        Returns:
            List[Pet]: A list of pets owned by the specified owner.
        """
        pass

    async def update_pet(
        self,
        pet_id: int,
        name: str | None = None,
        breed: str | None = None,
        age: int | None = None,
    ) -> Pet | None:
        """
        Updates information about a pet by its ID.

        Args:
            pet_id (int): The ID of the pet to be updated.
            name (Optional[str]): The new name of the pet, if provided.
            breed (Optional[str]): The new breed of the pet, if provided.
            age (Optional[int]): The new age of the pet, if provided.

        Returns:
            Optional[Pet]: The updated pet object if the update was successful, otherwise None.
        """
        pass

    async def delete_pet(self, pet_id: int) -> bool:
        """
        Deletes a pet by its ID.

        Args:
            pet_id (int): The ID of the pet to be deleted.

        Returns:
            bool: True if the pet was successfully deleted, otherwise False.
        """
        pass
