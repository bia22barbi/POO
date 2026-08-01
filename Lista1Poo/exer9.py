estoque = {}

def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    quantidade = int(input("Digite a quantidade em estoque: "))

    if titulo in estoque:
        estoque[titulo] += quantidade
    else:
        estoque[titulo] = quantidade
        print("Livro adicionado com sucesso.")

        def remover_livro():
            titulo = int(input("Digite a quantidade a remover:"))

            if titulo not in estoque:
                print("O livro não está no estoque.")

            elif quantidade > estoque[titulo]:
                print("Quantidade maior do que a disponível em estoque.")
            
            if  estoque[titulo] == 0:
                print("O estoque do livro ficou zerado")
            else:
                print("Quantidade removida com sucesso.")

        def consultar_livro():
            titulo = input("Digite o título do livro:")

            if titulo in estoque:
                print(f"Quantidade disponível: {estoque[titulo]}")
            else:
                print("O livro não está em estoque. ")

        def mostrar_estoque():
            if len(estoque) == 0:
                print("O estoque está vazio.")
            else:
                print("\n===== ESTOQUE =====")

                for titulo in sorted(estoque):
                    print(f"{titulo}: {estoque[titulo]} unidades")

        while True:

                 print("\n===== MENU =====")
                 print("1 . Adicionar livro")
                 print("2 . Remover livro")
                 print("3 . Consultar livro")
                 print("4 . Mostrar estoque")
                 print("5 . Sair")

                 opcao = input("Escolha uma opção: ")

                 if opcao == "1":
                            adicionar_livro()
                 elif opcao == "2":
                            remover_livro()
                 elif opcao == "3":
                            consultar_livro()
                 elif opcao == "4":
                            mostrar_estoque()
                 elif opcao == "5":
                   print("Programa encerrado.")
                 break
        
                 else:
                  print("Opção inválida. Tente novamente.")





