def fatorial(n):
    if (n < 0):
        return 0
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
    
def fatorial_recursivo(n):
    if (n < 0):
        return 0
    elif (n == 0):
        return 1
    else:
        return (n * fatorial_recursivo(n - 1))

# módulo principal (main)

n = int(input("Digite um número: "))
result = fatorial(n)
resultRecursivo = fatorial_recursivo(n)

print(f"O fatorial de {n} é: ", result)
print(f"O fatorial de {n} em execução recursiva é: ", resultRecursivo)
    