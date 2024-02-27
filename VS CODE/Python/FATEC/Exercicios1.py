import os
def execute():
    os.system("cls")
    exercicio = int(input("Que exercicio você gostaria de ver?\n1)soma\n2)metros\n3)salário\n4)mercadoria\n5)viagem\n6)celsius\n7)aluguel\n8)milhão\nResposta: "))

    #1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
    if exercicio == 1:
        os.system("cls")
        n1 = int(input("Digite o 1° número:\n"))
        n2 = int(input("Digite o 2° número:\n"))
        print("A soma é:",n1 + n2)

    #2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
    if exercicio == 2:
        os.system("cls")
        metros = float(input("Escreva medida em metros:\n"))
        milimetro = metros * 1000
        print("A medida", metros,"em metros é", milimetro,"em milimetros")

    #3) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário
    if exercicio == 3:
        os.system("cls")
        salario = float(input("Digite seu salário:\n"))
        porcentagem = 1.25
        aumento = salario * porcentagem
        porcentagem = porcentagem - 1
        print(f"Seu salário era de {salario} e com o aumente de{porcentagem: .0%} ficou {aumento}")

    #4) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
    if exercicio == 4:
        os.system("cls")
        mercadoria = float(input("Qual o valor da mercadoria?\n"))
        desconto1 = float(input("E qual a porcentagem de desconto? (escreva apenas o número)\n"))
        print("DESCONTO1", desconto1)
        print("VALOR INICIAL", mercadoria)
        desconto = 100 - desconto1
        print("DESCONTO 1", desconto)
        desconto = desconto / 100
        print("DESCONTO 2", desconto)
        mercadoria = mercadoria * desconto
        print("VALOR TOTAL", mercadoria)
        print(f"O desconto solicitado foi de {desconto1}%, então o valor total a se pagar fica de {mercadoria} reais")

    #5) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
    if exercicio == 5:
        os.system("cls")
        km = float(input('Insira a distância a percorrer: '))
        vel_media = float(input('Insira a velocidade média: '))
        h = km / vel_media
        print('O tempo da viagem de carro será de {h} horas')

    #6) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
    if exercicio == 6:
        os.system("cls")
        celsius = float(input("Insira a tempera em graus Celsius:(Apenas o numero)\n"))
        F = (9*celsius)/5 + 32
        print("A temperatura de",celsius,"graus celsius é igual a",F,"Fahrenheit")

    #7) Escreva um programa que |pergunte a quantidade de km percorridos por um carro alugado pelo usuário|, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
    if exercicio == 7:
        os.system("cls")
        km = float(input("Qual foi a quantidade de km percorridos?\n"))
        dias = int(input("E quantos dias você ficou com o carro?\n"))
        valor = (km * 0.15) + (dias * 60)
        print(f"Por conta dos {dias} dias quee você ficou com o carro e por ter rodado {km} km, a conta à pagar fica {valor} reais")

    #8) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
    if exercicio == 8:
        os.system("cls")
        print('O numero 2 elevado a um milhão é composto de ', len(str(2 ** 1000000)), 'digitos') 

###############################################################################################################################################################

if(__name__ == "__main__"):
    execute()