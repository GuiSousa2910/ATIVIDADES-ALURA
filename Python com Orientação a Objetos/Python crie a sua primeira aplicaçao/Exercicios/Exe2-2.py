idade = int(input('Sua idade: '))

if 0 > idade < 12:
    print('Criança')
elif 13 > idade < 18:
    print('Adolescente')
else:
    print("Adulto")