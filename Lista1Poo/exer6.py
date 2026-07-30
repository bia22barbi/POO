assentos = [False] * 10

def reserva():
    numero = int(input("Digite o número do assento:"))
    indice = numero - 1


    if assentos[indice] == False:
        assentos[indice] = True
        print("Assento reservado com sucesso!")
    else:
        print("Assento já reservado!")

def liberar():
    numero = int(input("Digite o número do assento: "))
    indice = numero - 1

    if assentos[indice] == True:
        assentos[indice] = False
        print("Assento liberado com sucesso!")
    else:
        print("Assento não está reservado!")

def mostrar_mapa():
    for i in range(10):
        if assentos[i] == True:
            print(f"Assento {i + 1} - Reservado")
        else:
            print(f"Assento {i + 1} - Disponível")

while True:

    print("\n1 - Reservar um assento")
    print("2 - Liberar um assento")
    print("3 - Mostrar mapa de assentos")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      reserva()
    elif opcao == 2:
        liberar()
    elif opcao == 3:
         mostrar_mapa()
    elif opcao == 4:
         print("Saindo do programa...")
         break
    else:
            print("Opção inválida.")
    