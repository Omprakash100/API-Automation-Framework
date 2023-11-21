from helpers.request_handler import RequestHandler
from utils.user_generator import generate_random_user
from config.config import Config


class UserHelper:
    @staticmethod
    def get_user_by_username(username, logger):
        endpoint = f"{Config.USER_ENDPOINT}/{username}"
        logger.info(f"Sending GET request to endpoint: {endpoint}")
        response = RequestHandler.send_request("GET", endpoint)
        logger.info(f"Received response: {response.text}")
        return response

    @staticmethod
    def create_user(logger):
        endpoint = f"{Config.USER_ENDPOINT}"
        user_data = generate_random_user()
        logger.info(f"Sending POST request to endpoint: {endpoint} with data: {user_data}")
        response = RequestHandler.send_request("POST", endpoint, json_data=user_data.object_to_json())
        logger.info(f"Received response: {response.text}")
        return user_data, response

    @staticmethod
    def update_user(user_data, logger):
        endpoint = f"{Config.USER_ENDPOINT}/{user_data.username}"
        user_data.firstName = "om"
        logger.info(f"Sending PUT request to endpoint: {endpoint} with data: {user_data}")
        response = RequestHandler.send_request("PUT", endpoint, json_data=user_data.object_to_json())
        logger.info(f"Received response: {response.text}")
        return user_data, response

    @staticmethod
    def delete_user(username, logger):
        endpoint = f"{Config.USER_ENDPOINT}/{username}"
        logger.info(f"Sending DELETE request to endpoint: {endpoint}")
        response = RequestHandler.send_request("DELETE", endpoint)
        logger.info(f"Received response: {response.text}")
        return response
