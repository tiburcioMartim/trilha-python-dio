contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}


CLIENTS = {
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
print(CLIENTS)
print("=" * 100)

copy = CLIENTS.copy()
copy["cpf"]["name"] = "Martim"
copy["cpf"]["nascimento"] = "02/12/1992"
print(copy)

print("=" * 100)
copy.clear()
print(copy)
print("=" * 100)