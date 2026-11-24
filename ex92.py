vetor1 = []
vetor2 = []

print("--- Vetor 1 (10 valores) ---")
for i in range(10):
    vetor1.append(int(input(f"Valor {i+1}: ")))

print("\n--- Vetor 2 (12 valores) ---")
for i in range(12):
    vetor2.append(int(input(f"Valor {i+1}: ")))

comuns = []
for valor in vetor1:
    if valor in vetor2 and valor not in comuns:
        comuns.append(valor)

comuns.sort(reverse=True)
print("\nValores comuns em ordem decrescente:", comuns)