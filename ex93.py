frase = input("Digite uma frase: ")

vogais_lista = "aeiouAEIOU"
consoantes_lista = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vogais = 0
consoantes = 0
outros = 0

for char in frase:
    if char in vogais_lista:
        vogais += 1
    elif char in consoantes_lista:
        consoantes += 1
    else:
        outros += 1

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"Outros caracteres: {outros}")