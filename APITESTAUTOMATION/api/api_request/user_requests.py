from api.api_request.request_handler import RequestHandler
from utils.user_generator import generate_random_user
from api.endpoints.user_endpoints import UserEndpoints
from api.helper.json_converter import serialize_object_to_json

class UserHelper:
    @staticmethod
    def get_user_by_username(username, logger):
        endpoint = UserEndpoints.get_user_by_username(username)
        logger.info(f"Sending GET request to endpoint: {endpoint}")
        response = RequestHandler.send_request("GET", endpoint)
        logger.info(f"Received response: {response.text}")
        return response

    @staticmethod
    def create_user(logger):
        endpoint = UserEndpoints.create_user()
        user_data = generate_random_user()
        logger.info(f"Sending POST request to endpoint: {endpoint} with data: {user_data}")
        response = RequestHandler.send_request("POST", endpoint, json_data=serialize_object_to_json(user_data))
        logger.info(f"Received response: {response.text}")
        return user_data, response

    @staticmethod
    def update_user_by_username(user_data, logger):
        endpoint = UserEndpoints.update_user_by_username(user_data.username)
        user_data.firstName = "om"
        logger.info(f"Sending PUT request to endpoint: {endpoint} with data: {user_data}")
        response = RequestHandler.send_request("PUT", endpoint, json_data=serialize_object_to_json(user_data))
        logger.info(f"Received response: {response.text}")
        return user_data, response

    @staticmethod
    def delete_user(username, logger):
        endpoint = UserEndpoints.delete_user(username)
        logger.info(f"Sending DELETE request to endpoint: {endpoint}")
        response = RequestHandler.send_request("DELETE", endpoint)
        logger.info(f"Received response: {response.text}")
        return response
