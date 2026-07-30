# Lista para armazenar as notas

notas = []

def adicionar_notas(notas):
    nome  = input("Nome do aluno; ")
    nota = float(input("Nota:"))
    disciplina = input("Disciplina:")

    notas.append((nome, nota, disciplina))
    print("Nota cadastrada com sucesso!")

    def melhor_aluno(notas):
         if len(notas) == 0:
              print("Nenhuma nota cadastrada.")
              return
         disciplinas = []
         for aluno in notas:
              if aluno[2] not in disciplinas:

                 disciplinas.append(aluno[2])
                 for disciplina in disciplinas:
                   maior = -1
                   melhor = ""

                 for aluno in notas:
                     if aluno[2] == disciplinas:
                         if aluno[1] > maior:
                             maior = aluno[1]
                             melhor = aluno[0]

         print(f"Disciplina:{disciplina}")
         print(f"Melhor aluno:{melhor}")
         print(f"Nota: {maior}")
         print()

         def consultar_aluno(notas):
                nome = input("Digete o nome do aluno: ")

                encontrou = False
                for aluno in notas:
                    if aluno[0].lower()== nome.lower():
                        print(f"Disciplina:{aluno[2]} - Nota: {aluno[1]}")
                        encontrou = True
                        if not encontrou:
                            print("Aluno não encontrado.")

                        def exibir_ordenadas(notas):
                            if len(notas) == 0:
                                print("Nenhuma nota cadastrada.")
                                return
                            ordenadas = sorted(notas,key=lambda x: x[1], reserve = True)

                            print("\nNotas em ordem descrecente:\n")
                            for aluno in ordenadas:
                                print("\n===== MENU =====")
                                print("1 - Adicionar nota")
                                print("2 - Mostrar melhor aluno por disciplina")
                                print("3 - Consultar notas por alunos")
                                print("4 - Exibir notas ordenadas")
                                print("5 - Sair")

                                opcao = input("Escolha uma opção: ")
                                if opcao == "1":
                                    adicionar_nota(notas)

                                elif opcao =="2":
                                    melhor_aluno(notas)

                                elif opcao =="3":
                                    consultar_aluno(notas)

                                elif opcao =="4":
                                    exibir_ordenadas(notas)

                                elif opcao == "5":
                                    print("Programa encerrado. ")
                                    break
                                else:
                                    print("Opção inválida.")
                        menu()

                        

                            