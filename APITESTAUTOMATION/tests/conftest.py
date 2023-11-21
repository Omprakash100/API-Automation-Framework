import pytest
from utils.logger import CustomLogger
from helpers.pet_helper import PetHelper
from helpers.user_helper import UserHelper
from helpers.response_verifier import ResponseVerifier
from config.config import Config

@pytest.fixture(scope="module")
def logger(request):
    logger = CustomLogger(request.module.__name__, f"log/{request.module.__name__}.log").get_logger()
    yield logger

@pytest.fixture
def get_pet(logger):
    def _get_pet(pet_id):
        get_response = PetHelper.get_pet_by_id(pet_id, logger)
        ResponseVerifier.check_response_status(get_response, expected_status_code=Config.EXPECTED_STATUS_CODE)
    return _get_pet

@pytest.fixture
def post_pet(logger):
    pet_data, create_response = PetHelper.create_pet(logger)
    ResponseVerifier.check_response_status(create_response, expected_status_code=Config.EXPECTED_STATUS_CODE)
    return pet_data

@pytest.fixture
def pet_update_test_environment(logger, post_pet, get_pet):
    pet_data = post_pet
    yield pet_data
    get_pet(pet_data.id)

@pytest.fixture
def pet_delete_test_environment(logger, post_pet, get_pet):
    pet_data = post_pet
    get_pet(pet_data.id)

    yield pet_data

    with pytest.raises(AssertionError):
        get_pet(pet_data.id)

@pytest.fixture
def get_user(logger):
    def _get_user(username):
        get_response = UserHelper.get_user_by_username(username, logger)
        ResponseVerifier.check_response_status(get_response, expected_status_code=Config.EXPECTED_STATUS_CODE)
    return _get_user

@pytest.fixture
def post_user(logger):
    user_data, create_response = UserHelper.create_user(logger)
    ResponseVerifier.check_response_status(create_response, expected_status_code=Config.EXPECTED_STATUS_CODE)
    return user_data

@pytest.fixture
def user_update_test_environment(logger, post_user, get_user):
    user_data = post_user
    yield user_data
    get_user(user_data.username)

@pytest.fixture
def user_delete_test_environment(logger, post_user, get_user):
    user_data = post_user
    get_user(user_data.username)

    yield user_data

    with pytest.raises(AssertionError):
        get_user(user_data.username)