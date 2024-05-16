# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

# Entrada
# Nome do usuário, número de telefone e plano.
# Ex: 
# Ana
# (11) 91111-1111
# Plano Essencial Fibra

# Saída
# Mensagem indicando que o usuário foi criado com sucesso.
# Ex: Usuário Ana criado com sucesso.

# TODO: Crie uma classe UsuarioTelefone.
class UsuarioTelefone:
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."
        
# TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
      
# A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
def __str__(self):
    return f"Usuário {self.nome} criado com sucesso."

# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)