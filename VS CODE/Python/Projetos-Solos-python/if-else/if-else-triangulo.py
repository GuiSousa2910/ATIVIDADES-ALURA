lado1 = 0
lado2 = 0
lado3 = 0

lado1 = int(input("Informe o tamanho do primeiro lado qualquer do triângulo em centímetros:\n"))
lado2 = int(input("Informe o tamanho do segundo lado qualquer do triângulo em centímetros:\n"))
lado3 = int(input("Informe o tamanho do terceiro lado qualquer do triângulo em centímetros:\n\n"))

if lado1 == lado2 == lado3:
    print("Esse triâgulo é considerado equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triâgulo é considerado isósceles")
elif lado1 != lado2 != lado3:
    print("Esse triâgulo é considerado escaleno")
