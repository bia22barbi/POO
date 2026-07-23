reais = float(input("Digite o valor em reais:"))

print   ("Escolha a moeda de conversao:")
print   ("1. Dólar")
print   ("2. Euro")
print   ("3. Libra")
print   ("4. Iene")

opcao = int(input("Digite o numero correspondente a moeda escolhida: "))

if opcao == 1:
    convertido = reais * 0.19
    print("valor em dólar:", convertido)

elif opcao == 2:
    convetido = reais *0.17
    print("valor em euro:", convertido)

elif opcao == 3:
    convertido = reais *0.15
    print("valor em Libra:",convertido)    

elif opcao == 4:
 convertido = reais *25
 print("valor em Iene:", convertido)

else:
    print("opcao inválida!")     