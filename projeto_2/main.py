# Usar como base o projeto 1
# Utilizar funções para saque, depósito e extrato.
# Criar função para cadastrar cliente e conta bancária.
# A função de saque deve receber valores apenas por keywords.
# A função de depósito deve receber valores apenas por posição.
# A função de extrato deve receber valores por keywords e por posição.
# Criar usuário deve receber nome, data de nasimento, cpf e endereço.
# Deve ser armazenado somente numeros do CPF.
# CPF não pode ser repetido.
# Endereço deve ser uma string no formato "logradouro - bairro - cidade/sigla_estado"
# Deve armazenar a conta em uma lista com as informações agência, numeroda conta e usuário.
# O número da conta é sequencial e a agência é fixa como "0001".
# O usuário pode ter mais de uma conta.
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
accounts = dict()
# cpf: [name, birth_date, address, accounts: list[account_number, agency, balance, transactions: list[value, type, date]]

def show_start_menu():
  print(start_menu)
  
def show_client_menu(client_name):
  print(f"Olá, {client_name}!")
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
  
def check_if_cpg_already_exists(cpf):
    return cpf in accounts
  
def register_client(cpf, name, birth_date, address):
  accounts[cpf] = {"name": name, "birth_date": birth_date, "address": address, "accounts": list()}

def create_account(client_cpf):
  # TODO: Get last overall account number
    client_account_number = str(len(accounts[client_cpf].get("accounts", [])) + 1).rjust(4, "0")
    client_agency = "0001"
    client_balance = 0
    client_transactions = []
    
    accounts[client_cpf]["accounts"].append({
      "account_number": client_account_number,
      "agency": client_agency,
      "balance": client_balance,
      "transactions": client_transactions
    })
    
    return client_account_number
  
def get_client_accounts(client_cpf):
  return accounts[client_cpf].get("accounts", [])

def deposit(client_cpf, account_number, value, /):
  account = next((account for account in accounts[client_cpf]["accounts"] if account["account_number"] == account_number), None)
  if account:
    account["balance"] += value
    account["transactions"].append({"value": value, "type": "deposit", "date": time.strftime("%d/%m/%Y %H:%M:%S")})
    
def withdraw(*, client_cpf, account_number, value):
  account = next((account for account in accounts[client_cpf]["accounts"] if account["account_number"] == account_number), None)
  if account["balance"] < value:
    return False
  
  if account:
    account["balance"] -= value
    account["transactions"].append({"value": value, "type": "withdraw", "date": time.strftime("%d/%m/%Y %H:%M:%S")})
    return True
  return False
  
def show_transactions(client_cpf, / , * , account_number):
  account = next((account for account in accounts[client_cpf]["accounts"] if account["account_number"] == account_number), None)
  if account:
    for transaction in account["transactions"]:
      print(f"{transaction['date']} - {transaction['type']} - R$ {transaction['value']:.2f}")
    
    print(f"Saldo atual: R$ {account['balance']:.2f}")

def mock_data():
  register_client("33377788899", "Thiago", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  register_client("22233344455", "Maria", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  register_client("11122233344", "João", "01/01/1990", "Rua 1 - Bairro 1 - São José dos Campos/SP")
  
  create_account("33377788899")
  create_account("33377788899")
  create_account("22233344455")
  create_account("11122233344")
  
# Main Program
mock_data()
while True:
  clear_screen()
  show_start_menu()
  start_menu_selected_option = input("Escolha uma opção: ")
  
  if start_menu_selected_option == '1':
    clear_screen()
    print("Cadastro de cliente\n")
    client_cpf = input("Digite o CPF: ").replace(".", "").replace("-", "")
    if check_if_cpg_already_exists(client_cpf):
      show_alert_message("CPF já cadastrado.")
      continue  
    
    client_name = input("Digite o nome: ")
    client_birth_date = input("Digite a data de nascimento: ")
    client_address = input("Digite o endereço no formato \"logradouro - bairro - cidade/sigla_estado\": \n")
    
    register_client(client_cpf, client_name, client_birth_date, client_address)    
    show_alert_message(f"Cliente {client_name} cadastrado com sucesso!")
    
  if start_menu_selected_option == '2':
    clear_screen()
    print("Cadastro de conta\n")
    client_cpf = input("Digite o CPF do cliente: ").replace(".", "").replace("-", "")
    if not check_if_cpg_already_exists(client_cpf):
      show_alert_message("CPF não cadastrado.")
      continue
    
    client_account_number = create_account(client_cpf)

    show_alert_message(f"Conta {client_account_number} cadastrada com sucesso!")
    
  # TODO: Implementar acesso a conta
  if start_menu_selected_option == '3':
    clear_screen()
    print("Acesso a conta\n")
    client_cpf = input("Digite o CPF do cliente: ").replace(".", "").replace("-", "")
    if not check_if_cpg_already_exists(client_cpf):
      show_alert_message("CPF não cadastrado.")
      continue
    
    client_acounts = get_client_accounts(client_cpf)
    if (not client_acounts) or (len(client_acounts) == 0):
      show_alert_message("Cliente não possui contas.")
      continue
    
    clear_screen()
    print("Contas cadastradas:")
    for account in client_acounts:
      print(f"Agência: {account['agency']} - Conta: {account['account_number']} - Saldo: {account['balance']}")
      
    selected_account_number = input("Digite o número da conta: ")
    
    if not any(account['account_number'] == selected_account_number for account in client_acounts):
      show_alert_message("Conta não encontrada.")
      continue
    
    while True:
      clear_screen()
      show_client_menu(accounts[client_cpf]["name"])
      print(f"Conta: {selected_account_number}")
      print(f"Saldo: {next((account['balance'] for account in client_acounts if account['account_number'] == selected_account_number), 0)}")
      client_menu_selected_option = input("Escolha uma opção: ")
      
      if client_menu_selected_option == '1':
        value = float(input("Digite o valor do saque: "))
        if withdraw(client_cpf=client_cpf, account_number=selected_account_number, value=value):
          show_alert_message(f"Saque realizado com sucesso no valor de R$ {value:.2f}.")
        else:
          show_alert_message("Saldo insuficiente.")
        
      elif client_menu_selected_option == '2':
        value = float(input("Digite o valor do depósito: "))
        deposit(client_cpf, selected_account_number, value)
        show_alert_message(f"Depósito realizado com sucesso no valor de R$ {value:.2f}.")
        
      elif client_menu_selected_option == '3':
        show_transactions(client_cpf, account_number=selected_account_number)
        input("\nPressione enter para continuar...")
        
      elif client_menu_selected_option == '4':
        show_alert_message("Saindo...")
        break
      
      else:
        show_alert_message("Opção inválida.")
        
    continue    
    
  if start_menu_selected_option == '4':
    clear_screen()
    print("Clientes cadastrados:")
    for cpf, client in accounts.items():
      print(f"CPF: {cpf} - Nome: {client['name']}")
    
    input("\nPressione enter para continuar...")
    
  if start_menu_selected_option == '5':
    exit_program()
    
  else:
    show_alert_message("Opção inválida.")