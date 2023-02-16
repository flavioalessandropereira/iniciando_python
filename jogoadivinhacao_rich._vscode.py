import random
import time
from rich import print



def linhas():
    print('[yellow]-=[/]' * 30)


linhas()
print('[blue]                JOGO DE ADIVINHAÇÃO[/]')
linhas()

pc = int(input('De 0 a ..., qual número quer estipular para ser adivinhado: '))
linhas()
adivinhar = random.randint(0, pc)

jogador = int(input('Em que número pensei: '))

linhas()

print('[green]PROCESSANDO ...[/]')
tempo = time.sleep(3)

linhas()

if jogador > pc:
    print('[red]Você jogou um número maior que o estipulado {}.[/]'.format(pc))
    linhas()
    exit()
if jogador == adivinhar:
    print('[bold][green]PARABÉNS! Você ganho![/]')
    linhas()
else:
    print('[red]VOCÊ PERDEU! Eu pensei no número {} e vc jogou o número {}.[/]'.format(
        adivinhar, jogador))
    linhas()
