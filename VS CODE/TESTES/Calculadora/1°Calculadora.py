
valor1 = float(input("Digite o primeiro valor:\n"))
valor2 = float(input("Digite o segundo valor:\n"))

tipo = int(input('''Selecione o número correspondente ao tipo de conta que deseja:
1) Soma.
2) Subtração.
3) Multiplicação.
4) Divisão.\n'''

"Resposta: "
))

resultado = 0

if tipo == 1 :
    print("SOMA")
    resultado = valor1 + valor2
elif tipo == 2:
    print("SUB")
    resultado = valor1 - valor2
elif tipo == 3:
    print("MUl")
    resultado = valor1 * valor2
elif tipo == 4:
    print("DVI")
    if valor2 == 0:
        print("NÃO É POSSIVEL DIVIDIR POR 0")
    resultado = valor1/valor2
else:
    print("DIGITO NÃO ACEITO!")

print("Resultado:", resultado)