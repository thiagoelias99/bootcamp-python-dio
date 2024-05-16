import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        print(f"Registrando saque de R$ {self._valor} na conta {conta.numero}")
        conta.sacar(self._valor)