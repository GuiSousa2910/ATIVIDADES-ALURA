notas = {'1º Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}
soma = 0
for nota in notas.values():
    soma += nota
print("Soma:",soma)

somatorio = sum(notas.values())
qntNotas = len(notas)
media = somatorio / qntNotas
print("Media:", round(media, 2))