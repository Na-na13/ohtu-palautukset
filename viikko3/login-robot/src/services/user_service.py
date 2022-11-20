import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if self._username_is_taken(username):
            raise AuthenticationError("Username is already taken")
        if len(username) < 3:
            raise AuthenticationError("Username must have min 3 characters")
        if not self._username_is_in_correct_form(username):
            raise AuthenticationError("Username can only consist of lowercase letters")
        if len(password) < 8:
            raise AuthenticationError("Password must have min 8 characters")
        if not self._password_is_in_correct_form(password):
            raise AuthenticationError("Password must include min 1 number or special character")
        
    def _username_is_taken(self, username):
        existing_user = self._user_repository.find_by_username(username)
        return existing_user

    def _username_is_in_correct_form(self, username):
        match = re.search("^[a-z]+$", username)
        return match

    def _password_is_in_correct_form(self, password):
        match = re.search("[^a-zA-Z]", password)
        return match