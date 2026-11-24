x = int(input("Digite o número inteiro X: "))

vetor = []
for i in range(32):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

ocorrencias = vetor.count(x)
print(f"O número {x} apareceu {ocorrencias} vez(es) no vetor.")