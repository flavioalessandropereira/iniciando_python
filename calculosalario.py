atual = float(input('Digite o seu salário atual: '))
reajuste = float(input('Qual a porecentagem de aumento? '))

valor_atual = atual + (atual*(reajuste/100))

print('A porcentagem de reajuste é de {:.2f}% e o salario atual reajustado é R${:.2f}'.format(reajuste,valor_atual))