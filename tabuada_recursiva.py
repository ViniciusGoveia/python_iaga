def tabuada(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

def tabuada_recursiva(i, n):
    if (i <= 10):
        print(f"{n} x {i} = {n * i}")
        i += 1
        tabuada_recursiva(i, n)
    else:
        print()

# módulo principal (main)
tabuada(7)
tabuada_recursiva(1, 7)