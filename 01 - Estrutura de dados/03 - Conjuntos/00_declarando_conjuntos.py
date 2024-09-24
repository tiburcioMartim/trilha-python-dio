numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
print(type(carros))

languages = {"python", "java", "python"}
print(languages)




carros = (("palio", "gol", "celta", "palio"))
carros = set(carros)
print(type(carros))