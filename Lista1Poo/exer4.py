def multiplos(x):
    for i in range(1, 101):
        if i % x == 0:
            print(i)

            x = int(input("Digite um número: "))
            multiplos(x)