import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        print(f"Registrando depósito de R$ {self._valor} na conta {conta.numero}")
        conta.depositar(self._valor)