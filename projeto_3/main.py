# Montar a modelagem de sistema conforme UML disponibilizado.
# Atualizar o aplocativo do projeto 2 para que ele possa ser utilizado com a modelagem de sistema.
from abc import ABC, abstractmethod

class Cliente:    
    _contas = list()
   
    def __init__(self, endereco):
        self._endereco = endereco

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])}"
      
    def registrar_conta(self, conta):
        self._contas.append(conta)
        
    def get_contas(self):
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco, data_nascimento):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])}"
        
class Conta:
  _contas = list()
  
  def __init__(self, cliente: Cliente, agencia: str):
    self._cliente = cliente
    self._agencia = agencia
    self._saldo = 0.0
    self._numero = len(self._contas) + 1
    self._contas.append(self)
    self._historico: Historico = Historico()
    
  def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])}"
    
  @property
  def saldo(self):
    return self._saldo
  
  @classmethod
  def nova_conta(cls, cliente: Cliente):
    conta = cls(cliente, '0001')
    cliente.registrar_conta(conta)
    return conta
  
  def sacar(self, valor: float):
    if valor > self._saldo:
      return False
    self._saldo -= valor
    self._historico.adicionar_transacao(Saque(valor))
    return True
  
  def depositar(self, valor: float):
    self._saldo += valor
    self._historico.adicionar_transacao(Deposito(valor))
    return True
  
class ContaCorrente(Conta):
  def __init__(self, cliente: Cliente, agencia: str, limite: float, limite_saque: int):
    super().__init__(cliente, agencia)
    self._limite = limite
    self._limite_saque = limite_saque
  
  @classmethod
  def nova_conta(cls, cliente: Cliente, * , limite = 500.0, limite_saque = 3):
    cls = cls(cliente, '0001', limite, limite_saque)
    cls._limite = limite
    cls._limite_saque = limite_saque
    return cls  
  
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass   
      
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def __str__(self) -> str:
       return f"Saque de R$ {self._valor}"
        
    def registrar(self, conta):
        print(f"Registrando saque de R$ {self._valor} na conta {conta.numero}")
        conta.sacar(self._valor)   
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def __str__(self) -> str:
        return f"Depósito de R$ {self._valor}"
        
    def registrar(self, conta):
        print(f"Registrando depósito de R$ {self._valor} na conta {conta.numero}")
        conta.depositar(self._valor)
        
class Historico:
  _transacoes = list[Transacao]()
  
  def adicionar_transacao(self, transacao: Transacao):
    self._transacoes.append(transacao)
    
  def __str__(self):
    return f"Total de transações: {len(self._transacoes)}"
    

# App
import os
import time

start_menu = """
Bem vindo ao ThiBank!

1 - Cadastrar cliente
2 - Cadastar conta
3 - Acessar conta
4 - Visualizar clientes
5 - Sair
"""

client_menu = """
1 - Sacar
2 - Depositar
3 - Visualizar extrato
4 - Sair
"""

clients_list = list[PessoaFisica]()
accounts_list = list[ContaCorrente]()

def show_start_menu():
  print(start_menu)
  
def show_client_menu(client: PessoaFisica):
  print(f"Olá, {client._nome}!")
  print(client_menu)

def exit_program():
  clear_screen()
  print("Até mais!, Obrigado por usar o ThiBank!")
  exit()
  
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def show_alert_message(message):
  clear_screen()
  print(message)
  time.sleep(1.5)
  clear_screen()
  
def check_if_cpf_already_exists(cpf):
  return cpf in [client._cpf for client in clients_list]

def get_client_by_cpf(cpf):
  return [client for client in clients_list if client._cpf == cpf][0]
  
def register_client(cpf, name, birth_date, address):
  new_client = PessoaFisica(name, cpf, address, birth_date)
  clients_list.append(new_client)
  
def create_account(client: PessoaFisica):
  new_account = ContaCorrente.nova_conta(client)
  accounts_list.append(new_account)

def get_client_accounts(client: PessoaFisica):
  return [account for account in accounts_list if account._cliente == client] 

def mock_data():
  mock_client_1 = register_client("33377788899", "Thiago", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  mock_client_2 = register_client("22233344455", "Maria", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  mock_client_3 = register_client("11122233344", "João", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  
  create_account(mock_client_1)
  create_account(mock_client_1)
  create_account(mock_client_2)
  create_account(mock_client_3)

mock_data()
while True:
  clear_screen()
  show_start_menu()
  start_menu_selected_option = input("Escolha uma opção: ")
  
  if start_menu_selected_option == '1':
    clear_screen()
    print("Cadastro de cliente\n")
    client_cpf = input("Digite o CPF: ").replace(".", "").replace("-", "")
    if check_if_cpf_already_exists(client_cpf):
      show_alert_message("CPF já cadastrado.")
      continue  
    
    client_name = input("Digite o nome: ")
    client_birth_date = input("Digite a data de nascimento: ")
    client_address = input("Digite o endereço no formato \"logradouro - bairro - cidade/sigla_estado\": \n")
    
    register_client(client_cpf, client_name, client_birth_date, client_address)    
    show_alert_message(f"Cliente {client_name} cadastrado com sucesso!")
    
  elif start_menu_selected_option == '2':
    clear_screen()
    print("Cadastro de conta\n")
    client_cpf = input("Digite o CPF do cliente: ").replace(".", "").replace("-", "")
    if not check_if_cpf_already_exists(client_cpf):
      show_alert_message("CPF não cadastrado.")
      continue
    
    cliente = get_client_by_cpf(client_cpf)
    client_account_number = create_account(cliente)

    show_alert_message(f"Conta {client_account_number} cadastrada com sucesso!")  
    
  if start_menu_selected_option == '3':
    clear_screen()
    print("Acesso a conta\n")
    client_cpf = input("Digite o CPF do cliente: ").replace(".", "").replace("-", "")
    if not check_if_cpf_already_exists(client_cpf):
      show_alert_message("CPF não cadastrado.")
      continue
    
    cliente = get_client_by_cpf(client_cpf)
    
    client_acounts = cliente.get_contas()
    if (not client_acounts) or (len(client_acounts) == 0):
      show_alert_message("Cliente não possui contas.")
      continue
    
    clear_screen()
    print("Contas cadastradas:")
    for account in client_acounts:
      print(f"Agência: {account._agencia} - Conta: {account._numero} - Saldo: {account._saldo}")
      
    selected_account_number = input("Digite o número da conta: ")
    
    if not any(account['account_number'] == selected_account_number for account in client_acounts):
      show_alert_message("Conta não encontrada.")
      continue
    
    while True:
      clear_screen()
      show_client_menu(cliente._nome)
      print(f"Conta: {selected_account_number}")
      print(f"Saldo: {next((account['balance'] for account in client_acounts if account['account_number'] == selected_account_number), 0)}")
      client_menu_selected_option = input("Escolha uma opção: ")
      
      if client_menu_selected_option == '1':
        value = float(input("Digite o valor do saque: "))
        # if withdraw(client_cpf=client_cpf, account_number=selected_account_number, value=value):
        show_alert_message(f"Saque realizado com sucesso no valor de R$ {value:.2f}.")
        # else:
          # show_alert_message("Saldo insuficiente.")
        
      elif client_menu_selected_option == '2':
        value = float(input("Digite o valor do depósito: "))
        # deposit(client_cpf, selected_account_number, value)
        show_alert_message(f"Depósito realizado com sucesso no valor de R$ {value:.2f}.")
        
      elif client_menu_selected_option == '3':
        # show_transactions(client_cpf, account_number=selected_account_number)
        input("\nPressione enter para continuar...")
        
      elif client_menu_selected_option == '4':
        show_alert_message("Saindo...")
        break
      
      else:
        show_alert_message("Opção inválida.")
        
    continue    
  
  elif start_menu_selected_option == '4':
    clear_screen()
    print("Clientes cadastrados:")
    for client in clients_list:
      print(client)
    
    input("\nPressione enter para continuar...")
  
  elif start_menu_selected_option == '5':
    exit_program()
    
  else:
    show_alert_message("Opção inválida.")