s1= 'Alura'
s2 = "Alura"
print(type(s1), type(s2))

texto = '  Guilherme de Sousa Agoskinho  '
print(texto.upper()) # deixa tudo maiusculo
print(texto.lower()) # deixa tudo minusculo
print(texto.strip()) # tira os espaços de antes e depois do texto
print(texto.replace('k', 't')) # substitui um caracter por outro
print(texto) # nao alterou a variavel em si

texto = texto.strip().replace('k', 't').upper()
print(texto) # agora sim a variavel sim esta alterada