from django.core import exceptions


class EmailAlreadyExists(Exception):
    message = 'This email already exists.'


class PasswordTooShort(Exception):
    message = 'Password is too short.'


class MustContainSpecialCharacter(Exception):
    message = 'Password must contain at least one special character.'

class AdminUserNameMustNotBeTaken(Exception):
    message = "Choose some other username. Admins' username cannot be taken"