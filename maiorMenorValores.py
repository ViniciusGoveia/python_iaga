from typing import List

def enumerarLista(lista: List[int]):
    listaOrdenada = sorted(lista)
    for index, numero in enumerate(listaOrdenada):
        print(f"x[{index}] = {numero}")

    return listaOrdenada

def informarMaiorEMenorValor(lista: List[int]):
    maiorValor = max(lista)
    menorValor = min(lista)

    posicaoMaiorValor = lista.index(maiorValor)
    posicaoMenorValor = lista.index(menorValor)

    print(f"Menor elemento, x[{posicaoMenorValor}] = {menorValor}")
    print(f"Maior elemento, x[{posicaoMaiorValor}] = {maiorValor}")

# módulo principal (main)

listaInput = []

for i in range(7):
    valor = int(input())
    listaInput.append(valor)

listaOrdenada = enumerarLista(lista=listaInput)

print("")

informarMaiorEMenorValor(lista=listaOrdenada)