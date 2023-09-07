import bola
import quadrado
import funcionario
import retangulo

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