import faker
from api.models.pet import Pet


def generate_random_pet():
    fake = faker.Faker()
    pet_data = {
        "id": fake.random_int(min=1, max=100000),
        "name": fake.word(),
        "photoUrls": [fake.image_url()],
        "status": fake.random_element(elements=('om', 'on'))
    }

    pet_object = Pet(**pet_data)

    return pet_object
