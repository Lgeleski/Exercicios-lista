vetor = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

x = int(input("Digite o número X que deseja buscar: "))

contador = 0
for num in vetor:
    if num == x:
        contador += 1

print(f"O número {x} aparece {contador} vez(es) no vetor.")