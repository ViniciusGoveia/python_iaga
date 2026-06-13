while True: #loop infinito
    n = 0
    while ((n % 2) == 0) or (n <= 0) and (n != -1):
        n = int(input("Tamanho da Matriz (número positivo e ímpar, -1 para encerrar):\n"))

    if (n == -1):
        break

    meio = n // 2
    print()
    for i in range(n):
        for j in range(n):
            if ((i == meio) and (j == meio)):
                print(" 0 ", end="")
            elif (i == j): # diagonal principal
                print(" 1 ", end="")
            elif ((i + j) == (n - 1)): # diagonal secundária
                print(" 2 ", end="")
            else:
                print(" * ", end="")
        
        print()
