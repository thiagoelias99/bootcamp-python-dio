class Cliente: 
    _contas = list()
     
    def __init__(self, endereco):
        self._endereco = endereco

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])}"
