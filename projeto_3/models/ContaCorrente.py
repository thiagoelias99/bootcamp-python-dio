import Conta
import Cliente

class ContaCorrente(Conta):
  def nova_conta(cls, cliente: Cliente, *, limite = 500.0, limite_saque = 3):
    super().nova_conta(cliente)
    cls._limite = limite
    cls._limite_saque = limite_saque
    
    return cls
