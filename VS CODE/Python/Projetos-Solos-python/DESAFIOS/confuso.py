a = int(input("Insira o 1° número:\n"))
b = int(input("Insira o 2° número:\n"))

soma = a + b

if soma > 20:
    print("Soma antes da alteração:", soma)
    print("Soma após a alteração:",soma + 8)
elif soma <= 20:
    print("Soma antes da alteração:", soma)
    print("Soma após a alteração:",soma - 5)