#pedir um numero real e mostrar somente e porcao inteira
import math
from math import trunc
p = float(input('informe um número real:'))
print('a porção inteira de {} é {}'.format(p, trunc(p)))

#trunc é um dos modulos da biblioteca math, utilizamos ele para mostrar somente primeiro número antes da virgula

#calcule a formula de baskhara de um triângulo retângulo e mos-tre o tamanho da hipotenusa
import math
cb = int(input('informe o tamanho do cateto b:'))
cc = int(input('informe o tamanho do cateto c:'))


#h = math.hypot(cc, cb) modulo para calcular a hipotenusa

h = (cb ** 2 + cc ** 2)
print('o valor da hipotenusa é {:.2f}'.format(math.sqrt(h)))

#informe o ângulo para mostrar o seno, cos e tan

import math
an = float(input('informe o ângulo:'))
#modulo do raio
sen1 = math.sin(math.radians(an))
#vai transformar o valor dado com parametro em raio

print('o seno de {} graus é {:.1f}'.format(an, sen1))

cos1 = math.cos(math.radians(an))

print('o cos de {} graus é {:.1f}'.format(an, cos1))

tan1 = math.tan(math.radians(an))

print('o tan de {} graus é {:.1f}'.format(an, tan1))