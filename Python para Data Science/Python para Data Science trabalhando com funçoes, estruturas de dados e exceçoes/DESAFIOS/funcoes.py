lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
print('Tamanho da lista:', len(lista))
print('Menor da lista:' , min(lista))
print('Maior da lista:' , max(lista))

numeroEscolhido = int(input('Fale um numero de 1 a 10: '))
def tabuada(escolhido):
    for i in range(1, 11):
        print(escolhido , 'x', i, '=', escolhido * i)
tabuada(numeroEscolhido)

listaNova = []
listaVelha = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
print(len(listaVelha))
def verificacao():
    for i in range(0, len(listaVelha)):
        print(listaVelha[i])
        if (listaVelha[i] % 3) == 0:
            listaNova.append(listaVelha[i])
    return listaNova
print(verificacao())

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = map(lambda x: pow(x, 2), lista)
print(list(quadrado))

listaNotas = []
i = 0
while len(listaNotas) < 5:
    i += 1
    nota = float(input(f'Digite a nota numero {i}: '))
    listaNotas.append(nota)

maior = max(listaNotas)
menor = min(listaNotas)
listaNotas.remove(maior)
listaNotas.remove(menor)
soma = sum(listaNotas)
media = soma / 3

print('Sua media é:', media)

notas = []
while len(notas) < 4:
    nota = float(input('Insira a nota: '))
    notas.append(nota)
maximo = max(notas)
minimo = min(notas)
media = sum(notas) / len(notas)
if media > 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maximo} pontos e a menor nota de {minimo} pontos e foi {situacao}")

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

reformulandoNome = map(lambda x: x.capitalize(), nomes)
reformulandoNome = list(reformulandoNome)
reformulandoSobrenome = map(lambda x: x.capitalize(), sobrenomes)
reformulandoSobrenome = list(reformulandoSobrenome)

for i in range(len(reformulandoNome)):
    print('Nome completo:',reformulandoNome[i] , reformulandoSobrenome[i])