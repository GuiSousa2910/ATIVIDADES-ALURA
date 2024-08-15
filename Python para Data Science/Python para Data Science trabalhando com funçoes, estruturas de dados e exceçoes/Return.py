# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]
def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo
print(media(notas))

# Notas do(a) estudante 
notas = [6.0, 7.0, 9.0, 5.0]
def boletim(lista):
    media = sum(lista) / len(lista)
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return (media, situacao)
print(boletim(notas))

media, situacao = boletim(notas)
print(media)
print(situacao)
print(f"O estudante atingiu uma média de {media} e foi {situacao}")