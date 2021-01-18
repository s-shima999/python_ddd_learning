"""
User
"""
from object.user_name import UserName


class User():
    """
    aaa
    """

    def __init__(
        self,
        uid: str,
        family_name: str,
        first_name: str
    ):
        self._id: str = uid
        self._name: UserName = UserName(family_name, first_name)

    @property
    def uid(self):
        """
        a
        """
        return self._id

    @property
    def name(self):
        """
        a
        """
        return self._name
