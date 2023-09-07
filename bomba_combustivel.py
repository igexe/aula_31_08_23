class BOMBA_COMBUSTIVEL:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo=tipo_combustivel
        self.valor=valor_litro
        self.quantidade=quantidade_combustivel

    def abastece_valor(self):
        abastece=float(input('\ndigite valor a abastecer com o combustivel\n'))
        abastece=abastece/self.valor
        if self.quantidade>=abastece:
            print('\nforam colocados '+str(abastece)+' litros desse combustivel')
            self.quantidade-=abastece
        else:
            abastece=self.quantidade*self.valor
            print('\nforam colocados apenas '+str(abastece)+' reais de combustivel dando '+str(self.quantidade)+' litros de combustivel')
            self.quantidade-=(abastece/self.valor)

    def abastece_litro(self):
        abastece=float(input('\ndigite quantos litros de combustivel você deseja\n'))
        if self.quantidade>=abastece:
            print('\nforam colocados '+str(abastece)+' litros de combustivel por '+str(abastece*self.valor)+' reais')
            self.quantidade-=abastece
        else:
            abastece=self.quantidade
            print('\nforam colocados '+str(abastece)+' litros de combustivel por '+str(abastece*self.valor)+' reais')
            self.quantidade-=abastece

    def muda_valor(self):
        valor=float(input('\ndigite novo valor para o combustivel\n'))
        self.valor=valor

    def muda_combustivel(self):
        tipo=input('\ndigite o tipo do combustivel para essa bomba\n')
        self.tipo=tipo

    def muda_quantidade(self):
        quantidade=float(input('\ndigite a quantidade de combustivel que tem nessa bomba\n'))
        self.quantidade=quantidade