import faker
import random
from api.models.user import User


def generate_random_user():
    fake = faker.Faker()
    user_status = random.randint(0, 1)

    user_data = {
        "id": fake.random_int(min=1, max=1000),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": user_status
    }

    user_object = User(**user_data)

    return user_object
