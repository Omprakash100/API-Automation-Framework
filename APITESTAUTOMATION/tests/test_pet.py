from helpers.pet_helper import PetHelper
from helpers.response_verifier import ResponseVerifier
from config.config import Config


class TestPetstore:
    def test_update_pet(self, logger, pet_update_test_environment):
        logger.info(f"Testing update_pet")

        updated_data, update_response = PetHelper.update_pet(pet_update_test_environment, logger)
        ResponseVerifier.check_response_status(update_response, expected_status_code=Config.EXPECTED_STATUS_CODE)

        logger.info("update_pet test passed successfully.")

    def test_update_pet_by_id(self, logger, pet_update_test_environment):
        logger.info(f"Testing update_pet_by_id")

        updated_data, update_response = PetHelper.update_pet_by_id(pet_update_test_environment.id, logger)
        ResponseVerifier.check_response_status(update_response, expected_status_code=Config.EXPECTED_STATUS_CODE)

        logger.info("update_pet_by_id test passed successfully.")

    def test_delete_pet(self, logger, pet_delete_test_environment):
        logger.info(f"Testing delete_pet")

        delete_response = PetHelper.delete_pet(pet_delete_test_environment.id, logger)
        ResponseVerifier.check_response_status(delete_response, expected_status_code=Config.EXPECTED_STATUS_CODE)

        logger.info("delete_pet test passed successfully.")
