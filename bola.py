class BOLA:
    def __init__(self, cor, circunferencia, material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material

    def troca_cor(self, nova_cor):
        self.cor=nova_cor

    def mostra_cor(self):
        print('a bola é da cor '+self.cor)