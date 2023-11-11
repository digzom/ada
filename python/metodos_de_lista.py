# tem um monte kk

lista = [1, 2, 3, 4, 5, 6]

lista.append(7) # insere no final

print(lista)

lista.insert(4, 10) # vai no índice 4 e adiciona o 10 lá, "empurrando" os outros para frente

print(lista)

lista2 = [3, 11, 22, 33]

lista.extend(lista2) # tipo um merge

print(lista)

lista.pop() # remove o último elemento

print(lista)

lista.pop(1) # remove o elemento do índice zero

print(lista)

lista.remove(3) # remove exatamente o elemento baseado no valor, sempre vai remover o primeiro que encontrar

print(lista)

lista.count(22) # vai dar 1. Conta quantas vezes o valor do parâmetro aparece na lista

lista.index(11) # pega o índice do elemento específico

lista.sort() # ordena crescente

print(lista)

lista.sort(reverse=True) # acho que não preciso te explicar

print(lista)


### FUNÇÕES

len(lista) # 9
sum(lista) # soma todos os números dentro da lista
max(lista) # retorna o maior valor
min(lista) # retorna o menor valor


