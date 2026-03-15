class Ingrediente :

    def __init__(self,name : str,price : float):
        self.__id = 0
        self.__name = name
        self.__price = price

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def set_id(self, id : int) -> None:
        self.__id = id

    def set_name(self, name : str) -> None:
        self.__name = name

    def set_price(self, price : float) -> None:
        self.__price = price

    def total_price(self,quantidade : int) -> float:
        return quantidade * self.__price