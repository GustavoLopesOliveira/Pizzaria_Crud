import pandas as pd
import repository.PizzaRepository
import repository.IngredienteRepository

def get_last_id_pizza() -> int :
    df = repository.PizzaRepository.get_pizzas()
    return df["id"].max()



def get_last_id_ingrediente() -> int :
    df = repository.IngredienteRepository.get_ingredientes()
    return df["id"].max()