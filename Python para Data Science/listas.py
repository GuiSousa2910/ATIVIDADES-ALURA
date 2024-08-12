lista = ['Fabricio Daniel', 9.5, 9, 8, True]
print(lista[3])
print(lista[-1])

lista[3] = 10

for i in lista:
    print(i)

print(len(lista))
print(lista[1:4])

lista.append('Adicionado') #adiciona elementos no final da lista
print(lista)

lista.extend([1, 2, 3]) # adiciona varios elementos no final da lista de um so vez
print(lista)

lista.remove([1, 2, 3]) # remove elementos especificos da lista