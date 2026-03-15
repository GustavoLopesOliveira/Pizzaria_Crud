
import pandas as pd

from model.Ingrediente import Ingrediente
from utils.last_id import get_last_id_ingrediente

ingredientes_arquivo = "../../.data/ingrediente.txt"

def add_ingrediente(ingrediente : Ingrediente) -> bool:
    try :
        data : dict = ingrediente.to_dict()
        new_id = get_last_id_ingrediente() + 1
        data["id"] = new_id
        df = pd.DataFrame(data)
        df.to_csv(ingredientes_arquivo,mode="a")
    except Exception :
        return False
    return True


def update_ingrediente(id : int,ingrediente_novo : Ingrediente) -> bool :
    try :
        df = get_ingredientes()
        df.loc[df["id"] == id] = ingrediente_novo.to_list()
        df.to_csv(ingredientes_arquivo,mode="w")
    except Exception:
        return False
    return True

def get_ingredientes() -> pd.DataFrame:
    return pd.read_csv(ingredientes_arquivo)

def remove_ingrediente(id : int) -> None :
    df = get_ingredientes()
    indice = df.loc[df["id"] == id].index
    new_df = df.drop(index = indice)
    new_df.to_csv(ingredientes_arquivo,mode="w")