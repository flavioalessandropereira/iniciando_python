nome = "flavIO"


print(nome.upper()) # tudo em maiúsculo
print(nome.lower()) # tudo em minúsuculo
print(nome.title()) # primeira letra em maiúscula


texto = "   ola, mundo!   "

print (texto)
print(texto.strip() + ".") # tira os espaços em brancos
print(texto.lstrip() + ".") #t ira os espaços em brancos da esquerda
print(texto.rstrip() + ".") # tira os espaços em brancos da direita

menu = "Python"

print('####' + menu + '####')

print(menu.center(14)) #centraliza o texto em 14 espços
print(menu.center(14, '#')) #centraliza o texto e coloca o carater # no lugar do espaço

print('-'.join(menu)) # P-y-t-h-o-n