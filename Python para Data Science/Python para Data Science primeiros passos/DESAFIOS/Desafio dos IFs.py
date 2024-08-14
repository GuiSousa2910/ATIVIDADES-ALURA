n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um numero: '))
if n1 > n2:
    print('O numero 1 é maior')
else:
    print('O numero 1 é maior')

porcentagem = float(input('Insira o percentual de crescimento da sua empresa: '))
if porcentagem > 0:
    print('Porcentagem positiva')
else:
    print('Porcentagem negativa')

letra = str(input('Insira uma letra: '))
listaVogais = 'a, e, i, o, u'
if letra.lower() in listaVogais:
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante')

v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
v3 = float(input('Insira o terceiro valor: '))
if v1 > v2 and v1 > v3:
    print('O valor 1 é maior')
elif v2 > v1 and v2 > v3:
    print('O valor 2 é maior')
else:
    print('O valor 3 é maior')

p1 = float(input('Insira o valor do primeiro produto: '))
p2 = float(input('Insira o valor do segundo produto: '))
p3 = float(input('Insira o valor do terceiro produto: '))
if p1 < p2 and p1 < p3:
    print('O produto 1 é mais barato')
elif p2 < p1 and p2 < p3:
    print('O produto 2 é mais barato')
else:
    print('O produto 3 é mais barato')

horario = str(input('Insira o seu turno de trabalho: '))
if horario.lower() == 'manhã':
    print('Bom Dia')
elif horario.lower() == 'tarde':
    print('Boa Tarde')
else:
    print('Boa Noite')

n1 = int(input('Insira um numero: '))
if (n1 % 2) == 0:
    print('É par')
else:
    print('É impar')   

