def media1():
    calculo = (10 + 8 + 9) / 3
    print(calculo)
media1()

def media2(n1, n2, n3):
    calculo = (n1 + n2 + n3) / 3
    print(calculo)
media2(3, 6, 9)

nota1 = 8
nota2 = 7
nota3 = 6
media2(nota1, nota2, nota3)

notas = [8.5, 9.0, 6.0, 10.0]
def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo

resultado = media(notas)
print(resultado)