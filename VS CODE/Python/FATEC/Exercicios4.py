import os
def execute():
    os.system("cls")
    exercicio = int(input("Que exercicio você gostaria de ver?\n1) Par ou Ímpar\n2) Qual é o nome?\n3) 'A'\n4) Soma\n5) Calculadora\n6) Calculadora Básica\n7) Produtos\nResposta: "))

#1- Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.
    if exercicio == 1:
        os.system("cls")
        n = int(input("Insira um número: "))
        if n % 2 == 0:
            print("Esse número é  par!")
        else:
            print("Esse número é ímpar!")

#2- Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.
    if exercicio == 2:
        os.system("cls")
        nome = str(input('Insira um nome: '))
        nome = nome.lower()
        if nome == "ana":
            print("True")
        else:
            print("False")

#3- Faça uma função/método para verificar e contar quantas letras **a** tem numa frase.
    if exercicio == 3:
        os.system("cls")
        frase = str(input("Escreva oque quiser: "))
        totalA = 0
        for letra in frase:
            if letra in ["a", "A"]:
                totalA += 1
        print(f"O total de letras A é {totalA}")

#4- Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.
    if exercicio == 4:
        os.system("cls")
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))
        print(n1,"+",n2,"=", n1 + n2)

#5- (Função com retorno com parâmetro) Faça um programa contendo algumas funções: a) Função para construir um menu de opções para uma calculadora: Menu de cálculos |1.   Número ao quadrado 2.   Número ao cubo 3.  Raiz do número 4.    Raiz cúbica do número Qual é a opção desejada?| b) Desenvolva uma função para cada opção de cálculo. Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.
    if exercicio == 5:
        os.system("cls")
        def quadrado(n):
            return n**2
        def cubo(n):
            return n**3
        def raizQ(n):
            return n ** (1/2)
        def raizC(n):
            return n ** (1/3)

        def main():
            ast = "*"*20
            msg = 0
            possiveis = [0, 1, 2, 3, 4]
            while msg in possiveis:
                msg = int(input(f"""
    Menu de cálculos
    {ast}
    1.   Número ao quadrado
    2.   Número ao cubo
    3.   Raiz do número
    4.   Raiz cúbica do número
    5.   Sair
    Qual é a opção desejada?
    """))
                n = int(input("Insira um número para a conta: "))
                os.system("cls")
                if msg == 1:
                    print(f"O quadrado de {n} é {quadrado(n)}")
                elif msg == 2:
                    print(f"O cubo de {n} é {cubo(n)}")
                elif msg == 3:
                    print(f"a Raiz quadrada de {n} é {raizQ(n)}")
                elif msg == 4:
                    print(f"a Raiz cubica de {n} é {raizC(n)}")
                elif msg == 5:
                    print("Saindo...")
                    break
        main()
#6- (Função com retorno com parâmetro) Faça um programa contendo algumas funções: a) Função para construir um menu de opções para uma calculadora: || *** Minha Calculadora ***  Digite um número.....: Digite outro número..:  + Soma dois números  - Subtrai dois números  * Multiplica dois números / Divide dois números Qual opção deseja? || b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno. Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.
    if exercicio == 6:
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
#7- Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.
    if exercicio == 7:
        os.system("cls")
        cod = int(input("Dgite o código do produto: "))
        nome = str(input("Qual o nome desse produto: "))
        preco = float(input("Qual o preço de '"+ nome +"': "))
        np = print(f"O novo preço de {nome} após o reajuste, ficou de {preco * 1.10} reais")

###############################################################################################################################################################

if(__name__ == "__main__"):
    execute()