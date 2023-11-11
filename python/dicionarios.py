# agora o bagulho fica louco => Dicionários

dicionario = []
dicionario = dict()

dicionario = {"nome": "Fulano", "sobrenome": "De Tal", "altura": 1.70, "idade": 31}


print(dicionario["nome"])  # Fulano

dicionario["programadro"] = True  # vai adicionar essa chave inexistente e o valor

print(dicionario)

dicionario["altura"] = 1.71  # editou o campo

print(dicionario)

for key in dicionario:  # por padrão pega a chave
    print(dicionario[key])


"peso" in dicionario # False
"altura" in dicionario # True
