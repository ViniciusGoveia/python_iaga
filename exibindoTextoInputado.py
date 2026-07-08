def exibirTextoInputado(texto: str):
    for index, letra in enumerate(texto):
        if (index == len(texto) - 1):
            print(f"{letra}")
        else:
            print(f"{letra} ", end="")

# módulo principal (main)

entrada = str(input())

for i in range(3):
    exibirTextoInputado(texto=entrada)