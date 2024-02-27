import os
#6- (Função com retorno com parâmetro) Faça um programa contendo algumas funções: a) Função para construir um menu de opções para uma calculadora: || *** Minha Calculadora ***  Digite um número.....: Digite outro número..:  + Soma dois números  - Subtrai dois números  * Multiplica dois números / Divide dois números Qual opção deseja? || b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno. Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.
os.system("cls")
def ar(n1):
    de = n1 - int(n1)
    if de == 0:
        return round(n1)
    elif de != 0:
        return n1
def ar2(n2):
    de2 = n2 - int(n2)
    if de2 == 0:
        return round(n2)
    elif de2 != 0:
        return n2  
        
def s(n1, n2):
    print(f"{ar(n1)} + {ar2(n2)} = {ar(n1)+ar2(n2)}")
def m(n1, n2):
    print(f"{ar(n1)} - {ar2(n2)} = {ar(n1)-ar2(n2)}")
def mu(n1, n2):
    print(f"{ar(n1)} x {ar2(n2)} = {ar(n1)*ar2(n2)}")
def d(n1, n2):
    if n2 != 0:
        resultado = n1/n2
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"{ar(n1)} / {ar2(n2)} = {resultado}")
    else:
        print("Não é possivel divisão com 0")

def main():
    msg = 0
    possibilidade = [0,1,2,3,4]
    while msg in possibilidade:
        print("*** Minha Calculadora ***")
        n1 = float(input("Digite um número.....: "))
        n2 = float(input("Digite outro número..: "))
        print("*************************")
        msg = int(input("""1) + Soma
2) - Subtração
3) x Multiplicação
4) % Divisão
5)   Sair
Qual opção deseja?...: """))   
        os.system("cls")
        if msg == 1:
            s(n1,n2)
        elif msg == 2:
            m(n1,n2)
        elif msg == 3:
            mu(n1,n2)
        elif msg == 4 :
            d(n1,n2)
        elif msg == 5:
            break
main( )