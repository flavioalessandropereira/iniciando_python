import random
from time import sleep


def layout():
  print( '=' *30)
  
layout()
print('Jogo JOKENPÔ')
layout()

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)


print ('''Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

layout()

jogador = int(input('Qual a sua jogada: '))

layout()

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ')
sleep(1)

layout()

print ('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))

layout()

if computador == 0:
    if jogador == 0:
      print('EMPATE')
    elif jogador == 1:
      print('JOGADOR VENCEU!')
    elif jogador == 2:
      print('COMPUTADOR VENCE')

elif computador == 1:
    if jogador == 0:
      print('COMPUTADOR VENCE')
    elif jogador == 1:
      print('EMPATE')
    elif jogador == 2:
       print( 'JOGADOR VENCE!')

elif computador == 2:
    if jogador == 0: 
      print('JOGADOR VENCE!')
    elif jogador == 1:
      print('COMPUTADOR VENCE')
    elif jogador == 2:
       print( 'EMPATE')