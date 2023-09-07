import retangulo
import ponto

def cria():
    largura:float=float(input('digite largura do retangulo\n'))
    altura:float=float(input('digite altura do retangulo\n'))
    vertice:str=input('digite qual o vertice inicial do retangulo\n')
    retangulo1=retangulo.RETANGULO(largura,altura,vertice)
    centro=ponto.PONTO(retangulo1.centro_largura,retangulo1.centro_altura)
    print('\nretangulo criado\n')