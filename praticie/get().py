"""Explicação do Método get()

Sintaxe:          dicionario.get(chave, valor_default)
chave:            a chave que você deseja buscar no dicionário.
valor_default:    (opcional) o valor que será retornado se a chave não for encontrada. Se não for especificado, o método retorna None."""

# 1 - Acesso Seguro a Valores:
"""data_1 = {
    "name": "Maria",
    "age": "32",
}
name = data_1.get("name")
age = data_1.get("age")
print(f"{name} tem {age} anos de idade.")
print()"""

# 2 - Valor Padrão se a Chave Não Existe:
'''data_2 = {"name": "Carlos"}
cidade = data_2.get("city", "unkown")
print(cidade) # saída: unkown
print()'''

# 3 - Contar Ocorrências:
'''contagem = {}
words = ["apple", "banana", "apple", "orange"]
for word in words:
    contagem[word] = contagem.get(word, 0) + 1
print(contagem)
print()'''

# 4 - Verificação de Existência:
'''config = {
    "modo": "dark",
    "volume": "70"
}
theme = config.get("theme", "default")
print(theme) # saída: default
print()'''

# 5 - Uso em Funções:
'''def get_price(products, name):
    return products.get(name, "Product not found.")

prices = {
    'banana': 1.50,
    'apple': 2.00,
    'orange': 1.80
}

print(get_price(prices, "banana"))
print()'''

# 6 - Atualizando Valores Condicionalmente:
'''inventory = {
    'pen': 10,
    'note': 5
}
print(inventory)

inventory['pen'] = inventory.get('pen', 0) + 5
print(inventory)
print()'''

# 7 - Trabalhando com Dados de Usuário:
'''users = {
    'user1': True,
    'user2': False
}

stats_user = users.get('user1', 'user not found')
print(stats_user)
print()'''

"""car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(car)

a = car.get("brand")
print(a)

b = car.get("price", 15000)
print(b)
print(car)"""
