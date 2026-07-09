from typing import List

def montarListaBinaria(tamanho: int):
    lista = []

    for i in range(tamanho):
        posicao = i + 1
        if (posicao % 2 == 0):
            lista.append(1)
        else:
            lista.append(0)

    return lista

def exibirLista(lista: List[int]):
    count = len(lista)
    print("{", end="")

    for index, numero in enumerate(lista):
        if (index == count - 1):
            print(f"{numero}", end="")
        else:
            print(f"{numero}, ", end="")
    
    print("}", end="")

# módulo principal (main)

tamanhoLista = int(input())

listaBin = montarListaBinaria(tamanho=tamanhoLista)
exibirLista(lista=listaBin)