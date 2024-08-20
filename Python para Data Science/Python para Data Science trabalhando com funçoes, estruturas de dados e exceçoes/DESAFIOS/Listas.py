lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
for i in range(len(lista_de_listas)):
    soma = sum(lista_de_listas[i])
    # print(soma)
    
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
for i in range(len(lista_de_tuplas)):
    # print(lista_de_tuplas[i][2])
    break
    
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
listaNova = []
for i in range(len(lista)):
    listaNova.append([i + 1, lista[i]])
# print(listaNova)

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
numeros = []
for i in range(len(aluguel)):
    if aluguel[i][0] == 'Apartamento':
        numeros.append(aluguel[i][1])
# print(numeros)

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
arrumado = {
    meses[i]: despesa[i]
    for i in range(len(meses))
}
# print(arrumado)

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
listaLimpa = []
for i in range(len(vendas)):
    if vendas[i][0] == '2022' and vendas[i][1] >= 6000:
        listaLimpa.append(vendas[i])
# print(listaLimpa)

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
situacao = ''

for i in range(len(glicemia)):
    if glicemia[i] <= 70:
        situacao = 'Hipoglicemia'
    elif glicemia[i] > 70 and glicemia[i] <= 99:
        situacao = 'Normal'
    elif glicemia[i] > 99 and glicemia[i] <= 125:
        situacao = 'Pré-diabetes'
    else:
        situacao = 'Diabetes'
    print(situacao, glicemia[i])