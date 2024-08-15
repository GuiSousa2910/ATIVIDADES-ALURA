nota = float(input('Digite a nota do estudante: '))

def qualitativa(x):
    return x + 0.5
print(qualitativa(nota))

qualitativo = lambda x: x + 0.5
print(qualitativo(nota))

# Recebendo as notas e calculando a média ponderável
n1 = float(input("Digite a 1ª nota do(a) estudante: "))
n2 = float(input("Digite a 2ª nota do(a) estudante: "))
n3 = float(input("Digite a 3ª nota do(a) estudante: "))

mediaPonderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5)/3
print(mediaPonderavel(n1, n2, n3))

# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5
notasAtt = map(lambda x: x + qualitativo, notas)
notasAtt = print(list(notasAtt))