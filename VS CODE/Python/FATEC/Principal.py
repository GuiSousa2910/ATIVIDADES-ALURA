import Exercicios1
import Exercicios2
import Exercicios3
import Exercicios4
import os

os.system("cls")
lista = int(input("Que lista de exercicio você gostaria de acessar?\n1) Lista de exercícios 1\n2) Lista de exercícios 2\n3) Lista de exercícios 3\n4) Lissta de exercícios 4\n"))

if lista == 1:
    os.system("cls")
    Exercicios1.execute()
elif lista == 2:
    os.system("cls")
    Exercicios2.execute()
elif lista == 3:
    os.system("cls")
    Exercicios3.execute()
elif lista == 4:
    os.system("cls")
    Exercicios4.execute()
