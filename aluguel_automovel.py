empresa = 'Vapt and Vupt - Aluguel de Automóveis'

print('*' *50)
print('{:^50}'.format(empresa))
print('*' *50)

# Entrada de dias e km rodados
dias_alugados = int(input('Quantos dias alugado: '))
km_rodados = float (input('Total de km rodados? '))

print('*' *50)

valor_diaria = float(input('Qual o valor da diária do automóvel alugado?'))
valor_km_rodado= float(input('Qual o valor do km rodado? '))

total_diaria = dias_alugados * valor_diaria
total_rodado = km_rodados * valor_km_rodado


print('*' *50)
print('{:^50}'.format(empresa))
print('*' *50)

print('dias alugados a pagar: R$ {:.2f}'.format(total_diaria))
print('km rodados a pagar: R$ {:.2f}'.format(total_rodado))

print('-'*50)
print('Totalizando: R${:.2f}'.format(total_diaria+total_rodado))

print('*' *50)
