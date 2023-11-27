from config.config import Config

class UserEndpoints:
    @staticmethod
    def get_user_by_username(username):
        return f"{Config.USER_ENDPOINT}/{username}"

    @staticmethod
    def create_user():
        return f"{Config.USER_ENDPOINT}"

    @staticmethod
    def update_user_by_username(username):
        return f"{Config.USER_ENDPOINT}/{username}"

    @staticmethod
    def delete_user(username):
        return f"{Config.USER_ENDPOINT}/{username}"