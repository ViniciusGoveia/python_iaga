def mostrarPalavrasDaFrase(frase: str):
    listaPalavras = frase.replace(".", "").split(" ")
    countPalavras = len(listaPalavras)

    mostrarContagemDePalavras(countPalavras)

    for index, palavra in enumerate(listaPalavras):
        posicaoPalavra = index + 1
        print(f"{posicaoPalavra}a. palavra = {palavra}")

def mostrarContagemDePalavras(count: int):
    print(f"Existem {count} palavras, são elas:")
    print("")

# módulo principal (main)

fraseInput = str(input())

mostrarPalavrasDaFrase(frase=fraseInput)