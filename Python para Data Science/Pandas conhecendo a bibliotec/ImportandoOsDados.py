import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

primeirasDez = dados.head(10)
#print(primeirasDez)

ultimasDez = dados.tail(10)
#print(ultimasDez)

tamanho = dados.shape
#print(tamanho)

nomesColunas = dados.columns
#print(nomesColunas)

informacoes = dados.info()
#print(informacoes)

#print(dados['Tipo'])
#print(dados[['Quartos', 'Valor']])

mediaDeTodosImvoeis = dados['Valor'].mean()
#print('Valor medio de todos os imoveis:',mediaDeTodosImvoeis)

mediaValorAgrupado = dados.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor').round(2)
mediaValorAgrupado.plot(kind='barh', figsize=(14, 10), color ='blue')

visualizacaoDosTiposImoveis = dados.Tipo.unique()
imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']
somenteImoveisComerciais = dados.query('@imoveis_comerciais in Tipo')
naoImoveisComerciais = dados.query('@imoveis_comerciais not in Tipo')

visualizacaoImoveisFiltrados = naoImoveisComerciais.Tipo.unique()
#print(visualizacaoImoveisFiltrados)

mediaValorAgrupadoFiltrado = naoImoveisComerciais.groupby('Tipo')[['Valor']].mean().sort_values('Valor').round(2)
mediaValorAgrupadoFiltrado.plot(kind='barh', figsize=(14, 10), color ='blue')
plt.show()

