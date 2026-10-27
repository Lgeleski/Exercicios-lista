print("programa para classificar idades")
print()

nomes = [""] * 7
idades = [0] * 7

for i in range(len(nomes)):
    nomes[i] = input(f"informe o nome da {i + 1}° pessoa: ")
    idades[i] = int(input(f"informe a idade da {i + 1}° pessoa: "))

print()
print("Pessoas com 18 anos ou mais")

for i in range(len(nomes)):
    if idades[i] >= 18:
        print(nomes[i])