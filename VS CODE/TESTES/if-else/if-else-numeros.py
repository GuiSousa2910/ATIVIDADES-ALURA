numero1 = int(input('Insira o primeiro numero:\n'))
numero2 = int(input('Insira o segundo numero:\n'))
numero3 = int(input('Insira o terceiro numero:\n'))

if numero1 > numero2 and numero1 > numero3:
    print('O primeiro numero é o maior')
elif numero2 > numero1 and numero2 > numero3:
    print('O segundo numero é maior')
else:
    print('O terceiro numero é maior')