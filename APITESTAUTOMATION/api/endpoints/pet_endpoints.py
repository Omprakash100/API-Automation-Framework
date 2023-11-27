from config.config import Config

class PetEndpoints:
    @staticmethod
    def get_pet_by_id(pet_id):
        return f"{Config.PET_ENDPOINT}/{pet_id}"

    @staticmethod
    def create_pet():
        return f"{Config.PET_ENDPOINT}"

    @staticmethod
    def update_pet():
        return f"{Config.PET_ENDPOINT}"

    @staticmethod
    def update_pet_by_id(pet_id):
        return f"{Config.PET_ENDPOINT}/{pet_id}"

    @staticmethod
    def delete_pet(pet_id):
        return f"{Config.PET_ENDPOINT}/{pet_id}"