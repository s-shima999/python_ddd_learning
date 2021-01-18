"""
ユーザーリポジトリインターフェース
"""
from abc import ABCMeta, abstractmethod

class IUserRepository(metaclass=ABCMeta):
    """
    bbb
    """

    def __init__(self) -> None:
        """
        a
        """

    @abstractmethod
    def find(self):
        """
        ccc
        """

    @abstractmethod
    def update(self):
        """
        ccc
        """

    @abstractmethod
    def delete(self):
        """
        ccc
        """
