print("programa para apresentar 11 valores")
print()

valores = [0] * 11

for i in range(len(valores)):
    valores[i] = int(input(f"informe o {i + 1}° valor: "))

print()
print("Valores informados:")

for i in range(len(valores)):
    print(valores[i])
    print("----------------")