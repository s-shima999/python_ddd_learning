"""
ユーザーリポジトリ
"""

from user.i_user_repository import IUserRepository
from user.user import User

class UserRepository(IUserRepository):
    """
    aaa
    """

    def find(self):
        """
        aaa
        """
        return self._value_to_user()

    def update(self):
        """
        bbb
        """

    def delete(self):
        """
        bbb
        """

    def _value_to_user(self)->User:
        """
        a
        """
        return User(
            "",
            "",
            ""
        )
