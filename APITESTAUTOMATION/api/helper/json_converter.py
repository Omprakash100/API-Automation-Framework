from api.models.pet import Pet
from api.models.user import User


def serialize_object_to_json(data_object):
    json_data = data_object.object_to_json()
    return json_data


def deserialize_json_to_user(api_response):
    user_object = User.json_to_object(api_response)
    return user_object


def deserialize_json_to_pet(api_response):
    pet_object = Pet.json_to_object(api_response)
    return pet_object
