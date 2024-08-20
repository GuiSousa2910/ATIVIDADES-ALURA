from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

def geraCodigo():
    return str(randint(0,999))

ra = []

for i in range(len(estudantes)):
    ra.append((estudantes[i], estudantes[i][0] + geraCodigo()))

print(ra)