from api.api_request.user_requests import UserHelper
from api.api_reponse.response_verifier import ResponseVerifier
from config.config import Config


class TestUser:
    def test_update_user_by_username(self, logger, user_update_test_environment):
        logger.info(f"Testing update_user")

        updated_data, update_response = UserHelper.update_user_by_username(user_update_test_environment, logger)
        ResponseVerifier.verify_status_code(update_response, expected_status_code=Config.EXPECTED_STATUS_CODE)

        logger.info("update_user test passed successfully.")

    def test_delete_user(self, logger, user_delete_test_environment):
        logger.info(f"Testing delete_user")

        delete_response = UserHelper.delete_user(user_delete_test_environment.username, logger)
        ResponseVerifier.verify_status_code(delete_response, expected_status_code=Config.EXPECTED_STATUS_CODE)

        logger.info("delete_user test passed successfully.")
