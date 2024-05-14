# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato
# A versão 1.0 do sistema trabalha apenas com 1 usuário, não sendo necessário identificar o numero da agência e conta.
# Todos os depósitos e saques são armazenados em uma lista, que é o extrato do usuário.
# Deve permitir 3 saques diários com limite máximo de R$ 500,00 por saque.
# Caso o usuário tente sacar mais que o limite, deve retornar uma mensagem de erro.

menu = """
1 - Sacar
2 - Depositar
3 - Visualizar extrato
4 - Sair
"""

extrato = []
saques = 0
saldo_atual = 0
limite_saques_diario = 3
limite_valor_saque = 500

print("Bem vindo ao ThiBank!")

while True:
  print(menu)
  opcao = input("Escolha uma opção: ")
  
  # Sacar
  if opcao == '1':
    if saques < limite_saques_diario:
      valor = float(input("Digite o valor do saque: "))
      if valor > 0 and valor <= limite_valor_saque and valor <= saldo_atual:
        extrato.append(-valor)
        saldo_atual -= valor
        saques += 1
        print(f"Saque realizado com sucesso no valor de R$ {valor:.2f}.")
      elif valor > saldo_atual:
        print("Saldo insuficiente.")
      elif valor > limite_valor_saque:
        print(f"Limite de saque por operação é de R$ {limite_valor_saque:.2f}.")
      else:
        print("Valor inválido.")
    else:
      print("Limite de saques diário excedido.")
      
  # Depositar
  elif opcao == '2':
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
      extrato.append(valor)
      saldo_atual += valor
      print(f"Depósito realizado com sucesso no valor de R$ {valor:.2f}.")
    else:
      print("Valor inválido.")
      
  # Visualizar extrato
  elif opcao == '3':
    if len(extrato) > 0:
      print("Extrato:")
      for item in extrato:
        if item > 0:
          print("Despósito".ljust(15," ") + f"R$ {item:.2f}")
        else:
          print("Saque".ljust(15," ") + f"R$ {item:.2f}")
    else:
      print("Extrato vazio.")
      
  # Sair
  elif opcao == '4':
    print("Obrigado por utilizar o ThiBank!")
    break
  
  # Opção inválida
  else:
    print("Opção inválida.")