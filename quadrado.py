class QUADRADO:
    def __init__(self, lado):
        self.lado=lado

    def muda_lado(self, tamanho):
        self.lado=tamanho

    def mostra(self):
        print('o quadrado tem tamnho de: '+str(self.lado)+' x '+str(self.lado))

    def mostra_area(self):
        print('o quadrado tem area igual a: '+str(self.lado*self.lado))