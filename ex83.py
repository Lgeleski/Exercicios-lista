print("programa para apresentar valores em ordem inversa")
print()

valores = [0] * 18

for i in range(len(valores)):
    valores[i] = int(input(f"informe o {i + 1}° valor: "))

print()
print("Valores em ordem inversa")

for i in range(len(valores) - 1, -1, -1):
    print(valores[i])