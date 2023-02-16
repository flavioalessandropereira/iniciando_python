import random
import time

def linhas():
  print('\033[33m-=\033[m' *30)


linhas()
print('\033[31m                JOGO DE ADIVINHAÇÃO\033[m')
linhas()

pc = int(input('\033[34mDe 0 a ..., qual número quer estipular para ser adivinhado: \033[m'))
linhas()
adivinhar = random.randint(0,pc)

jogador = int(input('\033[34mEm que número pensei: \033[m'))

linhas()

print('\33[7;37mPROCESSANDO ...\33[m')
tempo = time.sleep(3)

linhas()

if  jogador > pc:
  print('\33[1;35mVocê jogou um número maior que o estipulado {}.\33[m'.format(pc))
  linhas()
  exit()
if jogador == adivinhar:
  print('\33[1;32mPARABÉNS! Você ganho!\33[m')
  linhas()
else:
  print('\33[1;31mVOCÊ PERDEU! Eu pensei no número {} e vc jogou o número {}.\33[m'.format(adivinhar,jogador))
  linhas()