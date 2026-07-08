def formatarValorMonetario(valor: float):
    return (f"R$ {valor:.2f}")

def calcularValorDoDesconto(valor: float):
    return (valor * 0.1)

def calcularValorFinal(valorDoProduto: float, valorDoDesconto: float):
    return (valorDoProduto - valorDoDesconto)

# módulo principal (main)

valorInput = float(input())

valorDoProduto = formatarValorMonetario(valorInput)
valorDoDesconto = calcularValorDoDesconto(valorInput)

valorFinal = calcularValorFinal(valorDoProduto=valorInput, valorDoDesconto=valorDoDesconto)

print(f"Valor do Produto  = {valorDoProduto}")
print(f"Valor do Desconto = {formatarValorMonetario(valorDoDesconto)}")
print(f"Valor Final       = {formatarValorMonetario(valorFinal)}")

print(" ")
print(" ")



