import Cliente
import Historico
import Conta
import Saque
import Deposito

class Conta:
  _contas = list[Conta]()
  
  def __init__(self, cliente: Cliente, agencia: str):
    self._cliente = cliente
    self._agencia = agencia
    self._saldo = 0.0
    self._numero = len(self._contas) + 1
    self._contas.append(self)
    self._historico: Historico = Historico()
    
  @property
  def saldo(self):
    return self._saldo
  
  @classmethod
  def nova_conta(cls, cliente: Cliente):
    return cls(cliente, '0001')
  
  def sacar(self, valor: float):
    if valor > self._saldo:
      return False
    self._saldo -= valor
    self._historico.registrar_transacao(Saque(valor))
    return True
  
  def depositar(self, valor: float):
    self._saldo += valor
    self._historico.registrar_transacao(Deposito(valor))
    return True