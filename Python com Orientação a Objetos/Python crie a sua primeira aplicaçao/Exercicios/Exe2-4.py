x = float(input('Insira a coordenada X: '))
y = float(input('Insira a coordenada Y: '))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print("Segundo quafrante")
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('Está localizado no eixo de origem')

