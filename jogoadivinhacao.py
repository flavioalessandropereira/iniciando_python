import random
import time
def linhas():
  print('-=' *20)


linhas()
print('JOGO DE ADIVINHAÇÃO')
linhas()

pc = int(input('De 0 a xx, qual número a ser jogado: '))

adivinhar = random.randint(0,pc)

jogador = int(input('Em que número pensei: '))

if jogador == adivinhar:
  print('PARABÉNS! Você ganho!')
else:
  print('VOCÊ PERDEU! Eu pensei no número {} e vc jogou o número {}.'.format(adivinhar,jogador))