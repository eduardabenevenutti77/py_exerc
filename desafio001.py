#mostre o antecessor e sucessor de um número
num = int(input('digite um número'))
ant = num - 1
suc = num + 1
print('o antecessor é {} e o sucessor é {} do número {}'.format(ant, suc, num))

#mostre o dobro, o triplo e a raiz quadrada do número
n = int(input('informe um valor para a operação:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de {} é {}, \no triplo {} \ne a sua raiz é {:.2f}'.format(n, d, t, r))

#peça 2 notas e calcule e mostre a media do aluno
nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))
m = (nota1 + nota2) / 2
print('a média do aluno é {:.1f}'. format(m))

#calcule a area de uma parede e mostre a quantidade de tinta utilizada para a sua pintura, mas considerando que cada l
#pinta 2m
altura = float(input('qual é a altura da parede?'))
largura = float(input('qual é a largura?'))
area = (largura * altura)
print('a area é {} por m2'.format(area))

l = (area / 2)
print('a quantidade de tinta a ser gasta é {}l'.format(l))

#peça o preço e de 5% de desconto
preco = int(input('qual é o valor da peça?'))
des = 5 / 100 * preco
novo = preco - des
print('o desconto será de 5%, então o desconto sobre peça irá custar {} reais'.format(des))
print('o novo preço do produto será {} reais'.format(novo))
#peça o salário e de 15% de aumento
sa = float(input('qual é o seu salário?'))
aumento = 0.15 * sa
novo = sa + aumento
print('o seu salário terá um aumento de {:.2f}'.format(aumento))
print('o novo salário a ser recebido será de {:.2f} reais'.format(novo))