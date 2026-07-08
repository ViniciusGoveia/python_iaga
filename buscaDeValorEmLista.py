from typing import List

def procurarPorValorEmLista(valor: int, lista: List[int]):
    posicaoDoValor = -1
    valorEncontrado = -1
    valorFoiEncontrado = False

    for index, numero in enumerate(lista):
        if (numero == valor):
            posicaoDoValor = index
            valorEncontrado = numero
            valorFoiEncontrado = True
            break

    return (valorEncontrado, valorFoiEncontrado, posicaoDoValor)

# módulo principal (main)

valorParaBusca = int(input())

listaNumeros = [10, 2, 7, 8, 5, 3, 22, 17, 18]

print("{", end="")

for index, numero in enumerate(listaNumeros):
    if (index == len(listaNumeros) - 1):
        print(f"{index}:{numero}", end="")    
    else:
        print(f"{index}:{numero}, ", end="")

print("}", end="")

print("")
print("")

(valorEncontrado, 
 confirmaValorEncontrado,
 posicaoDoValor) = procurarPorValorEmLista(valor=valorParaBusca, lista=listaNumeros)

if (confirmaValorEncontrado):
    print(f"Item: {valorParaBusca}, foi encontrado na posicao {posicaoDoValor}.")
else:
    print(f"Item: {valorParaBusca}, \"nao\" foi encontrado.")
