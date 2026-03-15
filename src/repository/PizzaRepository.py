import pandas as pd
from pexpect import Expecter

from model.Pizza import Pizza
from utils.last_id import get_last_id_pizza

pizza_arquivo = "../../.data/pizza.csv"
ingredientes_arquivo = "../../.data/ingrediente.txt"


def get_pizzas() -> pd.DataFrame :
    df = pd.read_csv(pizza_arquivo)
    return df


def add_pizza(pizza : Pizza) -> bool :
    try :
        data = pizza.to_dict()
        new_id = get_last_id_pizza() + 1
        data["id"] = new_id
        df = pd.DataFrame(data)
        df.to_csv(pizza_arquivo,mode="a")
    except Exception:
        return False
    return  True
def update_piza(id : int, pizza : Pizza) -> bool :
    try :
        data = pizza.to_dict()


def remove_pizza(id : int) -> None :

