lista = [10,11,12,13,17,21,99,33,47,14,18,24,50,60,70,80]

for elemento in lista:
    pares = elemento % 2
    if pares == 0:
        par = pares + elemento
        print(par)
    
