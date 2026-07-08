def calcularDesconto(valor: float):
    multiplicadorDesconto = 1
    valorDoDesconto = 0
    if (valor < 5000.00):
        multiplicadorDesconto = 0.1
        valorDoDesconto = valor * multiplicadorDesconto
    else:
        multiplicadorDesconto = 0.15
        valorDoDesconto = valor * multiplicadorDesconto

    return (valorDoDesconto, multiplicadorDesconto)

def calcularValorFinal(valorProduto: float, valorDesconto: float):
    return (valorProduto - valorDesconto)

# módulo principal (main)

valorDoProduto = float(input())
(valorDoDesconto, multiplicadorDesconto) = calcularDesconto(valor=valorDoProduto)
valorFinal = calcularValorFinal(valorProduto=valorDoProduto, valorDesconto=valorDoDesconto)

print(f"Valor do Produto        = R$ {valorDoProduto:.2f}")
print(f"Valor do Desconto ({(multiplicadorDesconto * 100):.0f}%) = R$ {valorDoDesconto:.2f}")
print(f"Valor Final             = R$ {valorFinal:.2f}")
