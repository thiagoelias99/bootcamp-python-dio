import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco, data_nascimento):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])}"