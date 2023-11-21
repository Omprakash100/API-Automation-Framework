from helpers.request_handler import RequestHandler
from utils.pet_generator import generate_random_pet
from config.config import Config


class PetHelper:
    @staticmethod
    def get_pet_by_id(pet_id, logger):
        endpoint = f"{Config.PET_ENDPOINT}/{pet_id}"
        logger.info(f"Sending GET request to endpoint: {endpoint}")
        response = RequestHandler.send_request("GET", endpoint)
        logger.info(f"Received response: {response.text}")
        return response

    @staticmethod
    def create_pet(logger):
        endpoint = f"{Config.PET_ENDPOINT}"
        pet_data = generate_random_pet()
        logger.info(f"Sending POST request to endpoint: {endpoint} with data: {pet_data}")
        response = RequestHandler.send_request("POST", endpoint, json_data=pet_data.object_to_json())
        logger.info(f"Received response: {response.text}")
        return pet_data, response

    @staticmethod
    def update_pet(pet_data, logger):
        endpoint = f"{Config.PET_ENDPOINT}"
        new_name = "UpdatedPet"
        pet_data.name = new_name
        logger.info(f"Sending PUT request to endpoint: {endpoint} with data: {pet_data}")
        response = RequestHandler.send_request("PUT", endpoint, json_data=pet_data.object_to_json())
        logger.info(f"Received response: {response.text}")
        return pet_data, response

    @staticmethod
    def update_pet_by_id(pet_id, logger):
        endpoint = f"{Config.PET_ENDPOINT}/{pet_id}"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        new_name = "UpdatedPet"
        update_data = {"name": new_name}
        logger.info(f"Sending POST request to endpoint: {endpoint} with headers: {headers} and updated data: {update_data}")
        response = RequestHandler.send_request("POST", endpoint, headers=headers, data=update_data)
        logger.info(f"Received response: {response.text}")
        return update_data, response

    @staticmethod
    def delete_pet(pet_id, logger):
        endpoint = f"{Config.PET_ENDPOINT}/{pet_id}"
        logger.info(f"Sending DELETE request to endpoint: {endpoint}")
        response = RequestHandler.send_request("DELETE", endpoint)
        logger.info(f"Received response: {response.text}")
        return response
