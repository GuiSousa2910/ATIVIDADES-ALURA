import os
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome  = nome.title() 
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome}, {self._categoria}'
    
    @classmethod
    def listarRestaurantes(cls):
        os.system('cls')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {'Sem Avaliações!' if not restaurante.media_avaliacoes else str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')
 
    @property #permite que você acesse o método como se fosse um atributo, sem precisar chamá-lo como uma função
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alterarEstado(self):
        self._ativo = not self._ativo
        
    def receberAvaliacao(self, cliente, nota=None):
        avaliacao = Avaliacao(cliente, nota) if nota is not None else Avaliacao(cliente)
        self._avaliacao.append(avaliacao)
        
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return None
        else:
            somaDasNotas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qntNotas = len(self._avaliacao)
            media = round(somaDasNotas / qntNotas, 1)
            return media