# def divisao(n1, n2):
#     if n2 == 0:
#         raise ValueError('O divisor nao pode ser 0')
#     div = n1 / n2
#     return div
# try:
#     n1 = float(input('Digite o numero: '))
#     n2 = float(input('Digite o numero: '))
#     resultado = divisao(n1, n2)
# except ValueError as v:
#     print('Erro:' ,type(v), v)
# except TypeError as t:
#     print('Nao é possivel fazer conta com string\nErro: ', type(t), t)
# else:
#     print(resultado)
# finally:
#     print('Programa encerrado')


# idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
# try:
#     nome = input('Digite um nome para ser procurado na lista: ')
# except KeyError as k:
#     print('Esse nome nao existe na lista')
# else:
#     print('Idade:',idades[nome])
# finally:
#     print('Programa encerrado')

# listaNova = []
# lista1 = [4,6,7,9,10]
# lista2 = [-4,6,8,9]

# def listas(l1, l2):
    
#     if len(l1) != len(l2):
#         raise IndexError('Listas tem que ser do mesmo tamanho')
    
#     listaA = []
#     for i in l1:
#         if i == str:
#             raise TypeError('A lista nao pode ter String')
#         listaA.append(i)
#     listaNova.append(listaA)
    
#     listaB = []
#     for i in l2:
#         if i == str:
#             raise TypeError('A lista nao pode ter String')
#         listaB.append(i)
#     listaNova.append(listaB)
    
#     listaC = []
#     for i in range(len(l1)):
#         soma = l1[i] + l2[i]
#         listaC.append(soma)
#     listaNova.append(listaC)
#     return listaA, listaB, listaC

# try:
#     listas(lista1, lista2)
# except IndexError as i:
#     print(i)
# except TypeError as t:
#     print(t)
# else:
#     print(listaNova)
# finally:
#     print('Programa finalizado')
    
