class FUNCIONARIO:

    '''================================
    parte ex 3'''

    def __init__(self,nome,salario):
        self.nome:str=nome
        self.salario:float=salario

    def return_nome(self):
        return self.nome

    def return_salario(self):
        return self.salario

    '''================================
    parte ex 4'''

    def aumentar_salario(self,percentual):
        self.salario=(self.salario*(100+percentual))/100