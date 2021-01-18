"""
a
"""
from abc import ABCMeta, abstractmethod

from user.i_user_repository import IUserRepository
from user.user_domain_service import UserDomainService

class IUserReguistoryService(metaclass=ABCMeta):
    """
    a
    """

    def __init__(
        self,
        user_repository:IUserRepository,
        user_domain_service:UserDomainService
    ) -> None:
        """
        a
        """
        self.user_repository: IUserRepository = user_repository
        self.user_domain_service: UserDomainService = user_domain_service

    @abstractmethod
    def handle(self):
        """
        a
        """
