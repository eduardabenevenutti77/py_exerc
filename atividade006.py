#conversor de temperatura
c = float(input('informe a temperatura em celsius:'))
f = (c * 9 / 5) + 32
print('a temperatura em fahrenheit é: {:.1f} f'.format(f))

#alugue de carro
km0 = float(input('quantos km foram percorridos com o carro?'))
d0 = int(input('por quantos dias o carro foi alugado?'))
df = d0 * 60
kmf = km0 * 0.15
g = df + kmf
print('durante o periodo de {} dias que fora alugado foi gasto {} km, o valor a ser pago para locadora é de {:.2f} reais.'.format(d0, km0, g))