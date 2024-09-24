import os


def exibir_infos():
    print("""Sabor Express 

1. Cadastrar restaurante
2. Listar restaurante
3. Ativar / Desativar restaurante
4. Sair
""")


def retorneMenu():
    input('\nPressione ENTER para voltar ')
    main()


def subtitulo(texto):
    os.system('cls')
    print(texto, '\n')


def finalizar():
    subtitulo('Finalizando Programa...')


def opcaoInvalida():
    os.system('cls')
    print('Opção Inválida \n')
    retorneMenu()


restaurante = []


def cadastrar_restaurante():
    subtitulo('Cadastro de Restaurantes')

    nomeRestaurante = input('Insira o nome do restaurante: ')
    categoriaRestaurante = input(f'Insira a categoria do restaurante {nomeRestaurante}: ')

    dadosRestaurante = {'nome': nomeRestaurante, 'categoria': categoriaRestaurante, 'ativo': False}
    restaurante.append(dadosRestaurante)

    print(f'O restaurante {nomeRestaurante} foi cadastrado!\n')

    retorneMenu()

def printAtivado(index, status):
    print(f"{index + 1} - {restaurante[index]['nome'].center(15)} | {restaurante[index]['categoria'].center(15)} | {status}\n")

def mostrarRestaurantes():
    subtitulo('Listando Restaurantes')
    if len(restaurante) > 0:
        for i in range(0, len(restaurante)):
            if restaurante[i]['ativo']:
                printAtivado(i, 'Ativado')
            else:
                printAtivado(i, 'Desativado')
    else:
        print('Não existe um cadastro de restaurante!')
    retorneMenu()


def ativarRestaurante():
    subtitulo('Alterando estado do Restaurante')

    if len(restaurante) > 0:
        nomeRestaurante = input('Insira o nome do restaurante que deseja ativar ou desativar: ')
        for i in range(0, len(restaurante)):
            if restaurante[i]['nome'] == nomeRestaurante:
                if restaurante[i]['ativo'] == True:
                    restaurante[i]['ativo'] = False
                    print('Seu restaurante foi desativado!')
                else:
                    restaurante[i]['ativo'] = True
                    print('Seu restaurante foi ativado!')
            else:
                print('Restaurante não encontrado!')
        retorneMenu()
    else:
        print('Você não tem um restaurante cadastrado')
        retorneMenu()


def escolhendo_opcao():
    try:
        opcaoEscolhida = int(input("Escolha uma opção: "))

        if opcaoEscolhida == 1:
            cadastrar_restaurante()
        elif opcaoEscolhida == 2:
            mostrarRestaurantes()
        elif opcaoEscolhida == 3:
            ativarRestaurante()
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