import math

angulo = float(input('Digite o angulo: '))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cos = math.cos(radianos)
tang = math.tan(radianos)

print('O ângulo de {}º corresponde: \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(angulo,seno,cos,tang))