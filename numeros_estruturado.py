def mostrar(n):
    print("{", end=" ")
    for i in range(1, n + 1):
        print(i, end=" ")
    print("}", end="")

def somar(n):
    sm = 0
    for i in range(1, n + 1):
        sm += i
    return(sm)

def resultados(n):
    mostrar(n)
    print("soma =", somar(n))

n = int(input("n: "))

resultados(n)