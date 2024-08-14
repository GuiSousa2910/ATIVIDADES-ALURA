n1 = int(input('Insira o numero: '))
n2 = int(input('Insira o numero: '))
for n in range(n1 + 1, n2):
    print(n)
    n += 1

a = 4
b = 10
dias = 0
while a <= b:
    a *= 1.03
    b *= 1.015
    dias += 1
print(f"Vai levar {dias} dias.")

for validacao in range(1, 16):
    nota = int(input(f'{validacao} Insira a nota: '))
    if nota > 5 or nota < 0:
        while nota > 5 or nota < 0:
            nota = int(input(f'{validacao} Insira a nota: '))
            print('Nota invalida')
            if nota <= 5 or nota >= 0:
                continue
    else:
        validacao += 1

graus = 0
for numero in range(1, 10):
    temperatura = float(input('Insira a temperatura: '))
    if temperatura == -273:
        break
    graus += temperatura
    media = graus / numero
    print(f'Média: {media}')

n = int(input('Insira um numero: '))
for fatorial in range(n - 1, 0, -1):
    n = n * fatorial
print(n)

numero = int(input('Insira um numero: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')