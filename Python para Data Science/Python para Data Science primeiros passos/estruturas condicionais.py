media = float(input('Insira a media desse aluno: '))

if media >= 7:
    print('Passou!!')
elif media >= 6 and media < 7:
    print('Recuperação!')
else:
    print('Não passou.')