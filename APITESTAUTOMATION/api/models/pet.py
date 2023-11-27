class Pet:
    def __init__(self, id=None, category=None, name=None, photoUrls=None, tags=None, status=None):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status

    def __repr__(self):
        return f"Pet(id={self.id}, category={self.category}, name={self.name}, " \
               f"photoUrls={self.photoUrls}, tags={self.tags}, status={self.status})"

    def object_to_json(self):
        return self.__dict__

    @classmethod
    def json_to_object(cls, api_response):
        return cls(
            id=api_response.get('id'),
            category=api_response.get('category'),
            name=api_response.get('name'),
            photoUrls=api_response.get('photoUrls'),
            tags=api_response.get('tags'),
            status=api_response.get('status')
        )