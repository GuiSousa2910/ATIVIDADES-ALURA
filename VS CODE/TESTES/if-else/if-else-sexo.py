print('Escreva abaixo qual sexo você se indentifica, lembrando que use "M" para masculino e "F" para feminino.')
sexo = input()
sexo = sexo.upper()

if sexo == "M":
    print('Masculino')
elif sexo == "F":
    print('Feminino')
else:
    print('Sexo inválido!')