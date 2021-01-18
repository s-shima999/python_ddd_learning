class UserName():

    def __init__(
        self,
        famiry_name: str,
        first_name: str
    ) -> None:

        if famiry_name == "" or first_name == "":
            raise Exception("設定値が不正です。")

        self._famiry_name:str = famiry_name
        self._first_name:str = first_name

    @property
    def full_name(self):
        """
        a
        """
        return self._famiry_name + " " + self._first_name

    @property
    def famiry_name(self):
        """
        a
        """
        return self._famiry_name

    @property
    def first_name(self):
        """
        a
        """
        return self._first_name
