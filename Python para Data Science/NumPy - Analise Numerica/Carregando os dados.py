import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt('apples_ts.csv', delimiter = ',', usecols=np.arange(1, 88, 1))
print(dados)

print('Quantidade de tipos de dados nessa lista "Linhas e Colunas":',dados.ndim)
print('Quantos dados tem nela:',dados.size)
print('Quantidade de linhas e colunas respectivamente:',dados.shape)
dadoTransposto = dados.T
print('Transposição do array:',dadoTransposto)

datas = dadoTransposto[:, 0]
print('\n\nAqui pegamos so a primeira linha da tabela, as datas:\n',datas)

precos = dadoTransposto[:, 1:6]
print('\n\n Aqui estamos pegando os preços das maças correspondentes a cada data que pegamos acima:\n',precos)

datas = np.arange(1, 88) # assim faz com que os numeros fiquem como datas reais
grafico = plt.plot(datas, precos[:,0])
plt.show()

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

graficoMoscowAno1 = plt.plot(np.arange(1,13,1), Moscow_ano1)
graficoMoscowAno2 = plt.plot(np.arange(1,13,1), Moscow_ano2)
graficoMoscowAno3 = plt.plot(np.arange(1,13,1), Moscow_ano3)
graficoMoscowAno4 = plt.plot(np.arange(1,13,1), Moscow_ano4)
plt.legend(['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4'])
plt.show()

np.array_equal(Moscow_ano3, Moscow_ano4) #Isso mostra se os arrays sao iguais
np.allclose(Moscow_ano3, Moscow_ano4, 10) # Isso mostra se eles sao parecidos dentre um limite determinado

somaDeNans = sum(np.isnan(Kaliningrad))
arrumandoNan = np.mean([Kaliningrad[3], Kaliningrad[5]]) # faz uma media dos valores
Kaliningrad[4] = arrumandoNan
plt.plot(datas, Kaliningrad)
plt.show()