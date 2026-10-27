print("programa para separar pares e impares")
print()

valores = [0] * 12

for i in range(len(valores)):
    valores[i] = int(input(f"informe o {i + 1}° valor: "))

print()
print("Numeros pares")

for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i])

print()
print("Numeros impares")

for i in range(len(valores)):
    if valores[i] % 2 != 0:
        print(valores[i])