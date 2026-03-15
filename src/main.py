
def menu() -> None :
    print("1 - Obter Pizza",end="\n")
    print("2 - Adicionar Pizza",end="\n")
    print("3 - Editar Pizza", end="\n")
    print("4 - Excluir Pizza", end="\n")

    op = input("Informe o numero")

    match op:
        case "1" :
            return

if __name__ == "__main__":
    menu()