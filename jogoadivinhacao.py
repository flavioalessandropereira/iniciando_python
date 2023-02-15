import random
import time
def linhas():
  print('-=' *30)


linhas()
print('                JOGO DE ADIVINHAÇÃO')
linhas()

pc = int(input('De 0 a xx, qual número a ser jogado: '))

adivinhar = random.randint(0,pc)

jogador = int(input('Em que número pensei: '))

linhas()

print('PROCESSANDO ...')
tempo = time.sleep(3)

linhas()

if  jogador > pc:
  print('Você jogou um número maior que o estipulado {}. Parou o jogo.'.format(pc))
  linhas()
  exit()
if jogador == adivinhar:
  print('PARABÉNS! Você ganho!')
  linhas()
else:
  print('VOCÊ PERDEU! Eu pensei no número {} e vc jogou o número {}.'.format(adivinhar,jogador))
  linhas()