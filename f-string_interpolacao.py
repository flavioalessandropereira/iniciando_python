nome = "flavio"
idade = 45
profissao = "DEV"
linguagem = "Python"

dados = {"cor":"amarelo", "carro":"fusca"}

print(f"Olá', sou {nome}, tenho {idade} anos, trabalho como {profissao}, com a linguagem {linguagem}.")

print ("cor: {cor}, automovel:{carro}".format(**dados))