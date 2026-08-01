palestra_ia = set()
workshop_python = set()

def adicionar_aluno():
     nome = input("Dgite o nome do aluno:")
     evento = input("Digite o evento(IA ou python): ")

     if evento.lower() == "ia":
         palestra_ia.add(nome)
         print("Aluno adicionado à palestra de ia.IA. ")

     elif evento.lower() == "python":
          workshop_python.add(nome)
          print("Aluno adicionado ao whokshop de python.")

     else:
          print("Evento inválido.")

def mostrar_ambos():
    alunos = palestra_ia.intersection(workshop_python)

    print("\nAlunos que participaram dos dois eventos:")
    if len(alunos) == 0:
         print("Nenhum alluno participou dos dois eventos.")
    else:
        for aluno in alunos:
            print(aluno)

def mostrar_somente_ia():
     alunos = palestra_ia.difference(workshop_python)
     print("\nAlunos que participaram somente da palestra de IA:")
     if len(alunos) == 0:
          print("Nenhum aluno participou somente da palestra de IA.")   
     else:
           for aluno in alunos:
               print(aluno)
def mostrar_pelo_menos_um():
      alunos = palestra_ia.union(workshop_python)
      print("\nAlunos que participaram de pelo menos um evento:")
      if len(alunos) == 0:
           print("Nenhum aluno participou de nenhum dos eventos.")
      else:
             for aluno in alunos:
                print(aluno)
def verificar_aluno():
       nome = input("Digite o nome do aluno: ")
     if nome in palestra_ia and nome in workshop_python:
           print("O aluno participou dos dois eventos.")
     elif nome in palestra_ia:
           print("O aluno participou somente da palestra de IA.")
      elif nome in workshop_python:
          print("O aluno participou somente do workshop de python.")

     else:
      print("O aluno não participou de nenhum dos eventos.")
while True:
          print ("\n===== MENU =====")
          print("1 . Adicionar aluno a um evento")
          print("2 . Mostrar alunos que participaram dos dois eventos")
          print("3 . Mostrar alunos somente da palestra de IA")
          print("4 . Mostrar alunos que participaram pelo menos de um evento")
          print("5 . Verificar participação de um aluno")
          print("6 . Sair")

          opcao = input("Escolha uma opção: ")
          if opcao == "1":
               adicionar_aluno()

          elif opcao == "2":
               mostrar_ambos()

          elif opcao == "3":
               mostrar_somente_ia()

          elif opcao == "4":
               mostrar_pelo_menos_um()

          elif opcao == "5":
               verificar_aluno()

          elif opcao == "6":
               print("Programa encerrado.")
               break

          else:
               print("opcao inválida.")