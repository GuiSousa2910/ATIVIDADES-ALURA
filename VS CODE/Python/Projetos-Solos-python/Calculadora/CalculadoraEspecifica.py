import os
#5- (Função com retorno com parâmetro) Faça um programa contendo algumas funções: a) Função para construir um menu de opções para uma calculadora: Menu de cálculos |1.   Número ao quadrado 2.   Número ao cubo 3.  Raiz do número 4.    Raiz cúbica do número Qual é a opção desejada?| b) Desenvolva uma função para cada opção de cálculo. Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

os.system("cls")
def ar(n):
        de = n - int(n)
        if de == 0:
            return round(n)
        elif de != 0:
            return n
def quadrado(n):
    return ar(n**2)
def cubo(n):
        return ar(n**3)
def raizQ(n):
    return ar(n ** (1/2))
def raizC(n):
    return ar(n ** (1/3))

def main():
    ast = "*"*20
    msg = 0
    possiveis = [0, 1, 2, 3, 4]
    while msg in possiveis:
        msg = int(input(f"""
**Menu de cálculos**
{ast}
1.   Número ao quadrado
2.   Número ao cubo
3.   Raiz do número
4.   Raiz cúbica do número
5.   Sair
Qual é a opção desejada?
"""))
        if msg == 5:
             print("Saindo...")
             break
        n = float(input("Insira um número para a conta: "))
        os.system("cls")
        if msg == 1:
            print(f"O quadrado de {n} é {quadrado(n)}")
        elif msg == 2:
            print(f"O cubo de {n} é {cubo(n)}")
        elif msg == 3:
            print(f"a Raiz quadrada de {n} é {raizQ(n)}")
        elif msg == 4:
            print(f"a Raiz cubica de {n} é {raizC(n)}")
main()