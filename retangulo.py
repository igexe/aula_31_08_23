import ponto

class RETANGULO:

    def __init__(self, largura, altura,vertice_inicial):
        self.largura=largura
        self.altura=altura
        self.vertice_inicial=vertice_inicial

    def centro_largura(self):
        return self.largura/2
    
    def centro_altura(self):
        return self.altura/2
    
    def menu(self):
        action=int(input('\n1 para alterar dimensões do retangulo\n2 para exibir centro do retangulo\n3 para exibir dimensões do retangulo\n'))
        
        if action==1:
            largura:float=float(input('digite nova largura para o retangulo\n'))
            altura:float=float(input('digite nova altura para o retangulo\n'))
            self.altura=altura
            self.largura=largura
        
        elif action==2:
            centro=ponto.PONTO(self.centro_largura(),self.centro_altura())
            print(f"\nCentro: ({centro.x} , {centro.y})\n")
        
        elif action==3:
            print('as dimensões do retangulo são '+str(self.largura)+' x '+str(self.altura))
        
        else:
            pass