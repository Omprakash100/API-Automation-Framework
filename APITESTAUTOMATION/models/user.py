class User:
    def __init__(self, id=None, username=None, firstName=None, lastName=None,
                 email=None, password=None, phone=None, userStatus=None):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, firstName={self.firstName}, " \
               f"lastName={self.lastName}, email={self.email}, password={self.password}, " \
               f"phone={self.phone}, userStatus={self.userStatus})"

    def object_to_json(self):
        return self.__dict__

    @classmethod
    def json_to_object(cls, api_response):
        return cls(
            id=api_response.get('id'),
            username=api_response.get('username'),
            firstName=api_response.get('firstName'),
            lastName=api_response.get('lastName'),
            email=api_response.get('email'),
            password=api_response.get('password'),
            phone=api_response.get('phone'),
            userStatus=api_response.get('userStatus')
        )
