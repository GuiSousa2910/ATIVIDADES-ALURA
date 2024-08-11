contador = 1

while contador <= 10:
    print(contador)
    contador += 1

contador = 1
while contador <= 3:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input(f'Insira a nota de {nome}: '))
    n2 = float(input(f'Insira a nota de {nome}: '))
    print(f'Média é: {(n1+n2)/2}')
    contador += 1