import os

class ContaBancaria:
    conta = []
    
    def __init__(self, titular='', saldo=0):
        self._ativo = False
        self._titular = titular.title()
        self._saldo = round(saldo, 2)
        ContaBancaria.conta.append(self)
        
    def __str__(self):
        return f'{self._titular}, R$ {self._saldo}'
    
    @classmethod
    def listarContasBancarias(cls):
        os.system('cls')
        for conta in cls.conta:
            print(f'{conta._titular.ljust(10)} | R$ {conta._saldo} | {'Ativo' if conta._ativo else 'Inativo'}')
    
    def ativarConta(self):
        self._ativo = True
    
pessoa1 = ContaBancaria('João', 1000)
pessoa1.ativarConta()

pessoa2 = ContaBancaria('Maria', 2000)

ContaBancaria.listarContasBancarias()