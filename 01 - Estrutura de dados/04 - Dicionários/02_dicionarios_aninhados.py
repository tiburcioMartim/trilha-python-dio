contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1, "b": 2,},},
    "11276657912": {"name": "Martim", "phone": {"casa": "3868-6464", "celular": "21-98886-0136"},},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
extra = contatos["melaine@gmail.com"]["extra"]["b"] # 2
martim = contatos["11276657912"]["phone"]["celular"] #21-98886-0136

# print(martim)
# print(extra)
# print(telefone)
