saldo = 1000
while True:

     print("\n===== BANCO =====")
     print("1 - Depositar")
     print("2 - Sacar")
     print("3 - Consultar saldo")
     print("4 - Sair")

     opcao = int(input("Escolha uma opção"))

if opcao == 1:
     deposito = float(input("digite o valor do depósito: "))
     saldo = saldo + deposito
     print("Depósito realizado.")

elif opcao == 2:
    Saque = float(input("Digite o valor do saque:"))
    if saque<= saldo:
     saldo= saldo - saque
     print("Saldo realizado.")
    else:
     print("Saldo insuficiente.")
elif opcao == 3:
        print("Saldo atual: R$", saldo)

elif opcao == 4:
   print("Opcao inválida.")