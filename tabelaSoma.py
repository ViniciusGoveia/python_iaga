def montarTabelaDeSoma(valor: int):
    for i in range(10):
        valorSoma = valor + i
        print(f"x[{i}] = {valor} + {i} = {valorSoma}")

# módulo principal (main)

valorInput = int(input())

montarTabelaDeSoma(valor=valorInput)