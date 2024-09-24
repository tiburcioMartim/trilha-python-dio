contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# for chave in contatos:
#     print(chave, contatos[chave])

# print("=" * 100)

# for chave, valor in contatos.items():
#     print(chave, valor)






clientes = {
    "11177755511": {
        "name": "João",
        "nascimento": "01/12/1998",
        "phone": {
            "job": "3321-5667",
            "house": "2668-6464",
            "celular": "21-98885-0138",
        },
        "addres": {
            "job": {
                "rua": "Rua da Curva",
                "numero": "30",
            },
            "house": {
                "rua": "Rua de Cima",
                "numero": "23",
            },
        },
    },
    
    "cpf": {
        "name": "",
        "nascimento": "",
        "phone": {
            "job": "",
            "house": "",
            "celular": "",
        },
        "addres": {
            "job": {
                "rua": "",
                "numero": "",
            },
            "house": {
                "rua": "",
                "numero": "",
            },
        },
    },
}

for key in clientes:
    print("=" * 100)
    print(key, clientes[key])


for key, value in clientes.items():
    print("=" * 100)
    print(key, value)