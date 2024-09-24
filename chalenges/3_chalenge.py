def contar_caracteres(string):
    contador = {}
    for char in string:
        contador[char] = contador.get(char, 0) + 1
    return contador

# Solicita entrada do usuário
entrada = input("Digite um texto: ")
resultado = contar_caracteres(entrada)
print(resultado)






