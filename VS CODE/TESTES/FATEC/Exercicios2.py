import os
def execute():
    os.system("cls")
    exercicio = int(input("Que exercicio você gostaria de ver?\n1)triângulos\n2)João e os peixes\n3)maior número\n4)maior e menor número\n5)salário\nResposta: "))

#1- Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    if exercicio == 1:
        os.system("cls")
        l1 = int(input("Qual a medida do 1° lado do triângulo\n"))
        l2 = int(input("Qual a medida do 2° lado do triângulo\n"))
        l3 = int(input("Qual a medida do 3° lado do triângulo\n"))
        if l1 == l2 == l3:
            print("Triângulo equilátero")
        elif l1 != l2 and l1 != l3 and l2 == l3 or l2 != l1 and l2 != l3 and l1 == l3 or l3 != l1 and l3 != l2 and l1 == l2:
            print("Triâgunlo escaleno")
        elif l1 != l2 != l3:
            print("Triângulo isóceles")

#2- João, comprou um microcomputador para controlar o rendimento diário de seu trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca doestado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
    if exercicio == 2:
        os.system("cls")
        pesagem = int(input("João, você levará quantos quilos de peixe hoje?\n"))
        kgSP = 50
        if pesagem > kgSP:
            excesso =  pesagem - kgSP
            total  = 4 * excesso
            print("João, se você levar", pesagem,"kg de peixe, você terá de pagar",total,"reais por conta do excesso de",excesso,"kg")
        elif pesagem <= kgSP:
            print("Tudo certo João, você pode levar sua mercadoria de",pesagem,"kg sem se preocupar com multa por excesso!")

#3- Faça um Programa que leia três números e mostre o maior deles.
    if exercicio == 3:
        os.system("cls")
        n1 = float(input("Digite o 1° número\n"))
        n2 = float(input("Digite o 2° número\n"))
        n3 = float(input("Digite o 3° número\n"))

        maior =n1
        if n2 > maior:
            maior = n2
        elif n3 > maior:
            maior = n3
        print("O maior número é",maior)

#4- Faça um Programa que leia três números e mostre o maior e menor deles.
    if exercicio == 4:
        os.system("cls")
        n1 = float(input("Digite o 1° número\n"))
        n2 = float(input("Digite o 2° número\n"))
        n3 = float(input("Digite o 3° número\n"))

        maior =n1
        menor = n1
        if n2 > maior:
            maior = n2
        if n3 > maior:
            maior = n3
        if n2 < menor:
            menor = n2
        if n3 < menor:
            menor = n3
        print("O maior número é",maior,"e o menor é",menor)

#5- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto-Descontos = Salário Líquido. Calcule os descontos e o salário líquido.
    if exercicio == 5:
        os.system("cls")
        porHora = float(input("Quanto você recebe por hora?\n"))
        horaDia = int(input("Quantas horas você trabalha por dia\n"))
        salarioBruto = (porHora * horaDia) * 22
        inss = salarioBruto * 0.11
        impostoDeRenda = salarioBruto * 0.08
        sindicato = salarioBruto * 0.05
        salarioLiquido = salarioBruto - (inss + impostoDeRenda + sindicato)
        print("Você ganha",porHora,"por hora trabalhada e trabalha",horaDia," horas por dia então seu salário seria de",salarioBruto,"mas tendo de pagar",inss,"para o inss,",impostoDeRenda,"de imposto de renda e",sindicato,"para o sindicato, seu salário fica",salarioLiquido,"reais.")

###############################################################################################################################################################

if(__name__ == "__main__"):
    execute()