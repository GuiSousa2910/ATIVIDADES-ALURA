from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebidas
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Praça', 'Gourmet')
bebidaSuco = Bebidas('Melancia', 5.0, 'G')
pratoPao = Prato('Pão', 2.0, 'O melhor pão da cidade')

#restaurante1.alterarEstado()
#restaurante1.receberAvaliacao('Gui', 10)
#restaurante1.receberAvaliacao('Mario', 8.8)


#restaurante2 = Restaurante('Mexican Food', 'Mexicana')
#restaurante2.alterarEstado()
#restaurante2.receberAvaliacao('Rebeca')
#restaurante2.receberAvaliacao('Alessandro')


#restaurante3 = Restaurante('Japa', 'Japonesa')
#restaurante3.receberAvaliacao('Pedro', 10)
#restaurante3.receberAvaliacao('Gustavo', 2)
#restaurante3.receberAvaliacao('Gui', 4.5)
#restaurante3.receberAvaliacao('Vera', 8.8)


def main():
#    Restaurante.listarRestaurantes()
    pass

if __name__ == '__main__':
    main()