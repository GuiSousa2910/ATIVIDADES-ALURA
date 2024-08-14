import numpy as np
from random import choices
from random import randrange
import math

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print('Numero escolhido da lista:',choices(lista))

print('Numero aleatorio:',randrange(100))

n1 = int(input('Insira um numero: '))
n2 = int(input(f'O numero {n1} será elevado por: '))
print('Resultado =', pow(n1,n2))

qntPessoas = int(input('Insira a quantidade de pessoas que estão participando do sorteio: '))
print(f'A pessoa sorteada foi a numero {randrange(1, qntPessoas + 1)}!!')

token = randrange(1000, 9998, 2)
nome = str(input('Insira seu nome: '))
print(f'{nome} seu token é: {token}')

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
lista = []
for i in range(3):
    lista.append(choices(frutas))
print('Fruta escolhida:', lista)

area = float(input('Qual a area do seu jardim: '))
elevado = pow(area, 2)
total = (math.pi * elevado) * 25
print(f'O custo total para cercar o jardim é de R$ {total}')