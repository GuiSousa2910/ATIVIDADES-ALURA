class Restaurante:
    restaurantes = []
    
    def __init__(this, nome, categoria):
        this._nome  = nome.title()
        this._categoria = categoria.title()
        this._ativo = False
        Restaurante.restaurantes.append(this)
        
    def __str__(this):
        return f'{this._nome}, {this._categoria}'
    
    @classmethod
    def listarRestaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {restaurante.ativo}')
 
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alterarEstado(self):
        self._ativo = not self._ativo
    
    
restaurante_praca = Restaurante('Pracinha', 'Sujo')
restaurante_praca.alterarEstado()
restaurante_italiano = Restaurante('macarraozinho', 'Italiano')


Restaurante.listarRestaurantes()