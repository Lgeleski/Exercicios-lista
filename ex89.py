vetor = []
for i in range(10):
    num = int(input(f"Digite o número da posição {i}: "))
    vetor.append(num)

soma_impares = 0
mult_pares = 1

for i in range(len(vetor)):
    if i % 2 == 0:
        mult_pares *= vetor[i]
    else:
        soma_impares += vetor[i]

print(f"\nSoma dos valores nas posições ímpares: {soma_impares}")
print(f"Multiplicação dos valores nas posições pares: {mult_pares}")