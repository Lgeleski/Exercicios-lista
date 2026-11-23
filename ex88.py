alunos = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))

soma_notas = 0
for aluno in alunos:
    soma_notas += aluno[1]

media = soma_notas / len(alunos)
print(f"\nMédia da turma: {media:.2f}")

print("Alunos com nota menor que 7:")
for aluno in alunos:
    if aluno[1] < 7:
        print(f"- {aluno[0]} (Nota: {aluno[1]})")