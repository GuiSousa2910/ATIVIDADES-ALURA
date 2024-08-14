dicionario = {
    'chave': 1,
    'chave_2': 2,
}
print('Exemplo de dicionario:',dicionario)

cadastro = {
    'matricula': 1241029,
    'dias_cadstrado': 25,
    'mes_cadastrado': 10,
    'turma': '2E'
}
print('Cadastro completo:',cadastro)
print('Somente a matricula:',cadastro['matricula'])
print('Somente a turma:',cadastro['turma'])

cadastro['turma'] = '2G'
print('Turma após alteração:',cadastro['turma'])

cadastro['modalidade'] = 'EAD'
print('Adicionando modalidade no cadastro:',cadastro)

cadastro.pop('turma') #remove uma chave
print('Removendo turma do cadastro',cadastro)

print('Itens do cadastro:',cadastro.items())
print('Somente as chaves do cadastro:',cadastro.keys())
print('Somente os valores do cadastro:',cadastro.values())

for chaves in cadastro.keys():
    print(cadastro[chaves])

for valores in cadastro.values():
    print(valores)

for chaves, valores in cadastro.items():
    print(chaves, valores)