def linha():
    print('-=-' *20)

LIMITE_DIARIO = 500
LIMITE_SAQUES = 3
numero_saques = 0
saldo = 0
extrato = ''

linha()
print('{:^60}'.format('BANCO FTF'))



menu = '''
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
'''

while True:
    linha()
    print (menu)
    linha()

    print()
    opcao = input('Digite a operação desejada: ')
    print()

    if opcao == '1':
      linha()
      print('{:^30}'.format('DEPÓSITO'))
      valor = input('Valor a ser depositado: R$ ')

      if valor.strip():
        valor = float(valor)

        if valor >0 :  
          saldo += valor
          extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
          print('Falha na operação de DEPÓSITO.')



    elif opcao == '2':
      linha()
      print('{:^30}'.format('SACAR'))
      valor = input('Qual o valor a ser sadaco: R$ ')

      if valor.strip():
        valor = float(valor)
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_DIARIO 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
          print('Falha na operação de Saque. Saldo insuficiente.')

        elif excedeu_limite:
          print(f'Falha na operação de Saque. Limite R$ {LIMITE_DIARIO}/saque.')

        elif excedeu_saques:
          print(f'Falha na operação de Saque. {LIMITE_SAQUES}/dia.')

        elif valor > 0:
          saldo -= valor
          extrato += f'Saque R$ {valor:.2f}\n'
          numero_saques += 1
        
        else:
          print('Falha na operação. Informe um valor válido.')

    elif opcao == '3':
      linha()
      print('{:^50}'.format('************ EXTRATO ************'))
      print('\nSem movimentação na conta'if not extrato else extrato)
      print(f'\nSaldo R$ {saldo:.2f}')

    elif opcao == '0':
      linha()
      print('Saindo do Sistema Bancário!')
      break
    
    else:
      print('Operação inválida. Escolha alguma das oções do MENU.')
   
