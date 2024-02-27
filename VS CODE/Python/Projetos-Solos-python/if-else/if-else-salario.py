import os

salario = int(input("Informe seu salário:\n"))
salarioReal = 0 + salario

if salarioReal <= 280:
    porcentagem = 1.20
    salarioReal = int(salarioReal * porcentagem)
elif salarioReal >= 281 or salarioReal <= 700:
    porcentagem = 1.15
    salarioReal = int(salarioReal * porcentagem)
elif salarioReal >= 701 or salarioReal <= 1500:
    porcentagem = 1.10
    salarioReal = int(salarioReal * porcentagem)
elif salarioReal >= 1501:
    porcentagem = 1.05
    salarioReal = int(salarioReal * porcentagem)
os.system("cls")

porcentagem = porcentagem - 1
print("O salário antes do reajuste:\n", salario,"reais")
print(f"O percetual de aumento aplicado:\n {porcentagem: .0%}")
print("O valor do aumento foi:\n", salarioReal - salario,"reais")
print("O novo salário, após o aumento:\n", salarioReal,"reais")
