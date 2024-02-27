confirmação = str(input("Vamos fazer algumas perguntas sobre o caso, você está de acordo?\n"))
telefone = str(input("Você telefou para a vítima?\n"))
local = str(input("Você esteve no local do crime?\n"))
mora = input("Você mora perto da vítima?\n")
deve = input("Você devia para a vitima?\n")
trabalho = input("Você já trabalhou com a vítima?\n")

criminoso = 0
if telefone == "Sim" or "sim":
    criminoso = criminoso + 1
elif local == "Sim" or "sim":
    criminoso = criminoso + 1
elif mora == "Sim" or "sim":
    criminoso = criminoso + 1
elif deve == "Sim" or "sim":
    criminoso = criminoso + 1
elif trabalho == "Sim" or "sim":
    criminoso = criminoso + 1

if criminoso == 2:
    print("Você é considerado Suspeito.")
elif criminoso == 3 or 4:
    print("Você é considerado Cúmplice.")
elif criminoso == 5:
    print("Você está sendo condenado como Assassino.")