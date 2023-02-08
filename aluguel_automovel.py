dias_alugados = int(input('Quantos dias alugado: '))
km_rodados = float (input('Total de km rodados? '))

valor_diaria = float(input('Qual o valor da diária do automóvel alugado?'))
valor_km_rodado= float(input('Qual o valor do km rodado? '))

total_diaria = dias_alugados * valor_diaria
total_rodado = km_rodados * valor_km_rodado

empresa = 'Vapt and Vupt - Aluguel de Automóveis'

print('*' *50)
print('{:^50}'.format(empresa))
print('*' *50)

print('R$ km rodados: {:.2f}'.format(total_rodado))
print('R$ dias alugados: {:.2f}'.format(total_diaria))

print('-'*50)
print('Total pagar: R${:.2f}'.format(total_diaria+total_rodado))

print('*' *50)