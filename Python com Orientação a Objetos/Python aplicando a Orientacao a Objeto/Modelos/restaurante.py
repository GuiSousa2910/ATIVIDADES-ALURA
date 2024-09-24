class Restaurante:
    restaurantes = []
    
    def __init__(this, nome, categoria):
        this.nome  = nome
        this.categoria = categoria
        this.ativo = False
        Restaurante.restaurantes.append(this)
        
    def __str__(this):
        return f'{this.nome}, {this.categoria}'
    
    def listarRestaurantes():
        
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(15)} | {restaurante.categoria.ljust(15)} | {restaurante.ativo}')
 
restaurante_praca = Restaurante('Pracinha', 'Italiano')
restaurante_italiano = Restaurante('Macarraozinho', 'Italiano')

Restaurante.listarRestaurantes()