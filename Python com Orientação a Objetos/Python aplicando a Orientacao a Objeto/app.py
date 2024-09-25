from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.alterarEstado()
restaurante1.receberAvaliacao('Gui', 10)
restaurante1.receberAvaliacao('Mario', 8.8)


restaurante2 = Restaurante('Mexican Food', 'Mexicana')
restaurante2.alterarEstado()
restaurante2.receberAvaliacao('Rebeca')
restaurante2.receberAvaliacao('Alessandro')


restaurante3 = Restaurante('Japa', 'Japonesa')
restaurante3.receberAvaliacao('Pedro', 10)
restaurante3.receberAvaliacao('Gustavo', 2)
restaurante3.receberAvaliacao('Gui', 4.5)
restaurante3.receberAvaliacao('Vera', 8.8)


def main():
    Restaurante.listarRestaurantes()

if __name__ == '__main__':
    main()