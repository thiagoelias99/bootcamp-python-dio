import Conta
from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass