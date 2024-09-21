import os as os
from asyncio import wait_for


def exibir_infos():
    print("""Sabor Express 

1. Cadastrar restaurante
2. Listar restaurante
3. Ativar restaurante
4. Sair
""")


def retorneMenu():
    input('Precione ENTER para voltar')
    main()

def subtitulo(texto):
    os.system('cls')
    print(texto)

def finalizar():
    subtitulo('Finalizando Programa...')


def opcaoInvalida():
    os.system('cls')
    print('Opção Inválida \n')
    retorneMenu()


restaurante = []


def cadastrar_restaurante():
    subtitulo('Cadatro de Restaurantes')
    nomeRestaurante = input('Insira o nome do resturante: ')
    restaurante.append(nomeRestaurante)
    print(f'O restaurante {nomeRestaurante} foi cadastrado!\n')
    retorneMenu()


def mostrarRestaurantes():
    subtitulo('Listando Restaurantes')
    if len(restaurante) > 0:
        for i in range(0, len(restaurante)):
            print(f'{i + 1}. {restaurante[i]}\n')
    else:
        print('Não existe um cadastro de restaurante!')
    retorneMenu()


def escolhendo_opcao():
    try:
        opcaoEscolhida = int(input("Escolha uma opção: "))

        if opcaoEscolhida == 1:
            cadastrar_restaurante()
        elif opcaoEscolhida == 2:
            mostrarRestaurantes()
        elif opcaoEscolhida == 3:
            print(f"Você escolheu a opção ativar restaurante")
        elif opcaoEscolhida == 4:
            finalizar()
        else:
            opcaoInvalida()
    except ValueError:
        opcaoInvalida()


def main():
    os.system('cls')
    exibir_infos()
    escolhendo_opcao()


if __name__ == '__main__':
    main()
