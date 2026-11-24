frase = input("Digite uma frase: ")
letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

nova_frase = ""
for char in frase:
    if char in letras_validas:
        nova_frase += char
    else:
        nova_frase += "-"

print(nova_frase)