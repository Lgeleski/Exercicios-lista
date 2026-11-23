vetor_x = []
vetor_y = []

print("--- Preenchendo o vetor X ---")
for i in range(8):
    vetor_x.append(int(input(f"X[{i}]: ")))

print("\n--- Preenchendo o vetor Y ---")
for i in range(8):
    vetor_y.append(int(input(f"Y[{i}]: ")))

print("\n--- Resultados das multiplicações ---")
for i in range(8):
    resultado = vetor_x[i] * vetor_y[i]
    print(f"Posição {i}: {vetor_x[i]} * {vetor_y[i]} = {resultado}")