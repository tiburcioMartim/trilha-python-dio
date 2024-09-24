pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

pessoa["endereco"] = {"end1": "Rua 1", "end2": "Rua 2", "end3": "Rua 3", "end4": "Rua 4",}
print(pessoa)

pessoa["telefone"] = "1111-2222"
print(pessoa)