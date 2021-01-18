"""
メールアドレス
"""
class MailAddress():
    """
    a
    """

    def __init__(
        self,
        mail_address: str
    ) -> None:
        """
        コンストラクタ
        """
        self._mail_address: str = mail_address

    def __str__(self) -> str:
        """
        a
        """
        return self._mail_address
