nome = "Gui"
senha = 123

tentativa_nome = input('Insira o nome: ')
tentativa_senha = int(input('Insira a senha: '))

if nome == tentativa_nome and senha == tentativa_senha:
    print('Acesso permitido')
else:
    print('Acesso negado')