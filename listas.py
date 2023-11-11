# listas

# podemos criar listas de duas formas

lista = []
lista = list()

# listas podem ter quaisquer tipos de dados
# pretty much like elixir

lista = [25, 'Tanto faz', 3.42, 10, 40, 20, 300, 102, 'Eu']

print(lista[0]) # 25
print(lista[2]) # 3.42
# print(lista[3]) # erro
print(lista[-2]) # 'Tanto faz'
print(lista[1:3]) # ['Tanto faz', 3.42]
print(lista[1:]) # ['Tanto faz', 3.42, 10, 40, 20, 300, 102, 'Eu']
print(lista[1:7:2]) # ['Tanto faz', 10, 20] -> Esse terceiro argumento é o passo


for element in lista:
  print(element)

print('Comprimento da lista ', len(lista))
