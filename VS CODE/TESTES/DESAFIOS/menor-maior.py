n1 = int(input("Insira o 1° número\n"))
n2 = int(input("Insira o 2° número\n"))
n3 = int(input("Insira o 3° número\n"))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
   maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("Maior:", maior,"\nMenor:", menor)