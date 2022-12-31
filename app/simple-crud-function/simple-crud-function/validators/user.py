from pydantic import ConstrainedInt, ConstrainedStr


class UserFirstAndLastName(ConstrainedStr):
    min_length = 1
    max_length = 20


class UserName(ConstrainedStr):
    min_length = 1
    max_length = 60


class UserAge(ConstrainedInt):
    ge = 0
    le = 150


class UserAddress(ConstrainedStr):
    min_length = 1
    max_length = 200


class UserZipCode(ConstrainedStr):
    min_length = 1
    max_length = 50
