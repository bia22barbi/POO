tarefas = []
def adicionar_tarefa():
    tarefas = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)

def listar_tarefas():
    for tarefa in tarefas:
        print(tarefa)

def remover_tarefa():
    tarefa = input("Digite a tarefa que deseja remover:")

    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print("Tarefa removida.")
    else:
        print("Tarefa não encontrada.") 
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        remover_tarefa()
    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")





