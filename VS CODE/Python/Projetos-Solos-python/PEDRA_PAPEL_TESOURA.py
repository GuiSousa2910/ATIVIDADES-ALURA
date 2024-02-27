import os

def jogar():
    os.system("cls")
    nome1 = input("Jogador 1, digite seu nome: ")
    nome2 = input("Jogador 2, digite seu nome: ")
    os.system("cls")
    escolha1 = input(f"{nome1}, faça seu escolha. Pedra, papel ou tesoura: ")
    os.system("cls")
    escolha2 = input(f"{nome2}, faça seu escolha. Pedra, papel ou tesoura: ")
    os.system("cls")

    escolha1 = escolha1.lower()
    escolha2 = escolha2.lower()
    pedra = "pedra"
    tesoura = "tesoura"
    papel = "papel"


    if escolha1 == escolha2:
        print("Empatou")

    elif (escolha1 == pedra and escolha2 == tesoura) or (escolha1 == papel and escolha2 == pedra) or (escolha1 == tesoura and escolha2 == papel):
        print(f"{nome1} ganhou")

    elif (escolha2 == pedra and escolha1 == tesoura) or (escolha2 == papel and escolha1 == pedra) or (escolha2 == tesoura and escolha1 == papel):
        print(f"{nome2} ganhou")
        
    else:
        print("INVALIDO")
jogar()
escolha = input("\nGostaria de jogar de novo? Sim ou Não: ")
escolha = escolha.lower()
sim = "sim"
sim = sim.lower()
naos = ["Nao","nao","NAO","não","NÃO","Não"]
if escolha == naos:
    print("Até a proxima")
while escolha == sim:
    jogar()