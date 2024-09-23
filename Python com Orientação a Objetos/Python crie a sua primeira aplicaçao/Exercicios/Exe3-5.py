lista = [1,1,1,1,1,'a',1]
soma = 0
try:
    for i in range (0, len(lista)):
       soma += lista[i]
    print(soma)
except:
    print('Erro')