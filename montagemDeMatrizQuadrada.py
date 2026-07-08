def montarMatriz(tamanho: int):
    matriz = []

    for i in range(tamanho):
        linhaMatriz = []
        for j in range(tamanho):
            if (i == 0 or i == tamanho - 1):
                linhaMatriz.append("*")
            elif (j == 0 or j == tamanho - 1):
                linhaMatriz.append("*")
            else:
                linhaMatriz.append("@")
        matriz.append(linhaMatriz)

    return matriz

# módulo principal (main)

tamanhoMatriz = int(input())

matriz = montarMatriz(tamanho=tamanhoMatriz)

for linhaMatriz in matriz:
    for index, valorLinha in enumerate(linhaMatriz):
        if (index == tamanhoMatriz - 1):
            print(f"{valorLinha}")
        else:
            print(f"{valorLinha} ", end="")
