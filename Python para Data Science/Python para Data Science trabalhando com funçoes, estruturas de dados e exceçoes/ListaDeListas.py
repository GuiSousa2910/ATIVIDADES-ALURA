notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]
nomes = []
notasJuntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notasJuntas.append(notas_turma[i])
        
print(nomes)
print(notasJuntas)

notas = []
for i in range(0, len(notasJuntas), 3):
    notas.append([notasJuntas[i], notasJuntas[i+1], notasJuntas[i+2]])
print(notas)

print(notas[0][2])