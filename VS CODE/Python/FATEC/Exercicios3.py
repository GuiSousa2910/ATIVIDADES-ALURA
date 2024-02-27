import os
def execute():
    os.system("cls")
    exercicio = int(input("Que exercicio você gostaria de ver?\n1) Função sem retorno\n2) Percentual de aumento\n3) Média\n4) Multiplicar\n5) Subtração\n6) Reajuste\n7) Reajuste 2\n8) Média\nResposta: "))
                        
#1- Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.
    if exercicio == 1:
        os.system("cls")
        n = 0
        int(input("Insira um numero:\n"))
        if n > 0:
            n = 1
            print(n)
        elif n < 0:
            n = n
            print(n)

    #2- Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.   
    if exercicio == 2:
        os.system("cls")
        antigo = int(input("Qual o valor antigo deste item?\n"))
        atual = int(input("E qual o valor atual dele?\n"))
        preco = (atual - antigo)
        percentual = (preco / antigo) * 100
        print(f"Esse item teve um aumento de {percentual}% em seu valor")

#3- Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a *A*, deverá calcular a média aritimética das notas dos alunos, se for *P*, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final. |N1, N2 e N3 são notas | P1, P2 e P3 são pesos. | Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)|
    if exercicio == 3:
        os.system("cls")
        N1 = int(input("Insira a primeira nota do seu aluno: "))
        N2 = int(input("Insira a segunda nota do seu aluno: "))
        N3 = int(input("Insira a terceira nota do seu aluno: "))
        media = input("Que tipo de média deseja fazer? Digite 'A' para calcular uma média aritimética e 'P' para média ponderada: ")
        media = media.lower()
        if media == "a":
            mA = (N1 + N2 + N3) / 3
            print("A média é de", mA)
        elif media == "p":
            P1 = 5
            P2 = 3
            P3 = 2
            mP = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)
            print("A média é de", mP)

#4- Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.
    if exercicio == 4:
        os.system("cls")
        n = float(input("Insira um número: "))
        print(n,"x 2 =", n*2)

#5- Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.
    if exercicio == 5:
        os.system("cls")
        n1 = float(input("Insira um número para subtração: "))
        n2 = float(input("Insira outro número: "))
        print(n1,"-",n2,"=", n1 - n2)

#6- Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.
    if exercicio == 6:
        os.system("cls")
        preco = float(input("Insira o preço deste produto: R$ "))
        reajuste = preco * 1.09
        print("O produto de R$", preco,"sofreu um reajuste de 9% e ficou", reajuste)

#7- Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada pelo usuário.
    if exercicio == 7:
        os.system("cls")
        preco = float(input("Informe o preço do produto:R$ "))
        reajuste = int(input("Agora informe a porcentagem de reajuste: "))
        reajuste = (reajuste / 100)
        np = preco * reajuste
        np = np + preco
        print(f"O produto de {preco} reais sofreu um reajuste em seu preço, assim ficou {np} reais")

#8- Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.
    if exercicio == 8:
        os.system("cls")
        p1 = float(input("Insira a nota 1 do aluno: "))
        p2 = float(input("Insira a nota 2 do aluno: "))
        media = (p1+p2)/2
        if media >= 7:
            print(f"Com a média de {media} o aluno está aprovado!")
        else:
            print(f"Com a média de {media} o aluno está reprovado.")

###############################################################################################################################################################

if(__name__ == "__main__"):
    execute()