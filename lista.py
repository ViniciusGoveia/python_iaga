n = int(input("Tamanho da lista?: "))

print()

soma = 0
l = []
for i in range(n):
    item = int(input(f"{i+1}o. item da lista: "))

    soma = soma + item
    l.append(item)

print()
# 1a. forma: print da lista
print(l, "soma = ", soma)

print()
#2a. forma: print com for each
for item in l:
    print(item, end=", ")

print("soma = ", soma)
print()