t1 = t2 = True
f1 = f2 = False

nome = "Guilherme"
lista = 'Guilherme, Darci, Duda, Ana'

if t1 and t2:
    print('Expressão Verdadeira')
else:
    print('Expressão Falsa')

if f1 or t2:
    print('Expressão Verdadeira')
else:
    print('Expressão Falsa')

if not t2:
    print('Expressão Verdadeira')
else:
    print('Expressão Falsa')

if  nome in lista:
    print(f'o nome {nome} está na lista')
else:
    print(f'o nome {nome} nao está na lista')
