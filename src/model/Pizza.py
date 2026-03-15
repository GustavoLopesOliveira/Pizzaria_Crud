class Pizza :

    def __init__(self,sabor : str,price : float):
        self.__id = 0
        self.__sabor = sabor
        self.__price = price

    def get_id(self) -> int:
        return self.__id

    def get_sabor(self) -> str:
        return self.__sabor

    def get_price(self) -> float:
        return self.__price

    def set_id(self,id : int) -> None:
        self.__id = id

    def set_sabor(self,sabor : str) -> None:
        self.__sabor = sabor

    def set_price(self,price : float) -> None:
        self.__price = price