def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    
    if len(lista) > 4:
        raise ValueError('A lista não pode ter mais de 4 notas')
    return calculo

try:
    notas = [4, 5, 6, 1, '3']
    resultado = media(notas)
except TypeError as e:
    print("Não foi possivel fazer contas com String")
except ValueError as e:
    print("A lista não pode ter mais de 4 notas")
else:
    print(resultado)
finally:
    print("Fim do programa")