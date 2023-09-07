import bola
import quadrado
import funcionario
import retangulo
import bomba_combustivel as bomba

print('ex 1\n')

bola1=bola.BOLA("azul",5.5,"borracha")

bola1.mostra_cor()

bola1.troca_cor("vermelha")

bola1.mostra_cor()

print('\n=====================================\nex 2\n')

quadrado1=quadrado.QUADRADO(8.5)

quadrado1.mostra()

quadrado1.mostra_area()

quadrado1.muda_lado(2)

quadrado1.mostra()

quadrado1.mostra_area()

print('\n=====================================\nex 3 e 4\n')

harry=funcionario.FUNCIONARIO('Harry',25000)

print('o funcionario '+harry.nome+' recebe '+str(harry.salario))

harry.aumentar_salario(10)

print('com o aumento salarial de 10% o funcinario '+harry.nome+' passou a receber '+str(harry.salario))

print('\n=====================================\nex 5\n')

retangulo1=retangulo.RETANGULO(5,5,'superior direito')

retangulo1.menu()

retangulo1.menu()

retangulo1.menu()

retangulo1.menu()

print('\n=====================================\nex 6\n')

bomba1=bomba.BOMBA_COMBUSTIVEL('gasolina', 5.7, 1000)

bomba1.abastece_litro()

print('sobrou '+str(bomba1.quantidade))

bomba1.abastece_valor()

print('sobrou '+str(bomba1.quantidade))

bomba1.muda_valor()

bomba1.muda_quantidade()

print(bomba1.quantidade)
print(bomba1.valor)

bomba1.abastece_valor()

bomba1.muda_quantidade()

bomba1.abastece_litro()

print(bomba1.tipo)

bomba1.muda_combustivel()

print(bomba1.tipo)