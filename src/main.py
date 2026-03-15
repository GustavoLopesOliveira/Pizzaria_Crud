
def menu() -> None :
    print("1 - Obter Pizza",end="\n")
    print("2 - Adicionar Pizza",end="\n")
    print("3 - Editar Pizza", end="\n")
    print("4 - Excluir Pizza", end="\n")

    print("5 - Obter Ingrediente",end="\n")
    print("6 - Adicionar Ingrediente",end="\n")
    print("7 - Editar Ingrediente",end="\n")
    print("8 - Excluir Ingrediente",end="\n")

    print("0 - Efetuar Compra",end="\n")

    op = input("Informe o numero")

    match op:
        case "1" :
            return

if __name__ == "__main__":
    menu()