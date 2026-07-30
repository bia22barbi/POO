palestra_ia = set()
    workshop_python = set()

    def adicionar_aluno():
          nome = input("Dgite o nome do aluno:"))
    evento = input("Digiteo evento(IA ou python): ").lower()

     if evento == "ia":
         palestra_ia.add(nome)
         print("Aluno adicionado à palestra de ia.IA. ")
    elif evento == "python":
    workshop_python.add(nome)
    print("Aluno adicionado ao whokshop de python.")

    else:
    print("evento inválido.")

 def mostrar_ambos():
    ambos = palestra_ia & workshop_python

    print("Alunos que participaram dosdois eventos:")
    print(ambos)

 def mostrar_somente_ia():
        somente_ia = palestra_ia - workshop_python

        print("Alunos que participaram de pelo menos um evento: ")
        print(participantes)

        def verificar_aluno():
             nome = input("Digite o nome do aluno:")

    elif nome in palestra_ia:
     print("O aluno participou somente da palestra de IA.")

else:
print("O aluno não participou de nenhum dos eventos.")

def menu()
     while True:
          print ("\n===== MENU =====")
          print("1 - Adicionar aluno a um evento")
          print("2 - Mostrar alunos que participaram dos dois eventos")
          print("3 - Mostrar alunos somente da palestra de IA")
          print("4 - Mostrar alunos que participaram pelo menos de um evento")
          print("5 - Verificar participação de um aluno")
          print("6 - Sair")

          opcao = input("")
