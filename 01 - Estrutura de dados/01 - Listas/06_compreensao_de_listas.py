# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
#        retorno    iteração   iteravel      filtro
print(pares)

# version in for
numbers = [1, 30, 21, 2, 9, 65, 34]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even)







# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

# version in for
numbers = [1, 30, 21, 2, 9, 65, 34]
square = []
for number in numbers:
    square.append(number ** 2)
print(square)