#leia um numero de 0 a 9999 cada um de seus digitos separados
num = int(input("informe um número:"))

#n = str(num) #transforma a variável de valor inteiro numa string

u = num // 1 % 10
#divide o número por 1 - depois divide por dez, o resto dessa divisão será a unidade

d = num//10 % 10
#inves de dividir por 1 iremos dividir por 10, pois assim ele dará o valor da dezena

c = num//100 % 10
#o % pega só o primeiro valor que corresponde a centena/dezena/milhar/unidade, ex: 1985 - u: 5 | d: 8 | c: 9 | m: 1

m = num//1000 % 10

print('analisando o número {}'.format(num))
print('unidades {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))

#mostra na tela o valor do número, a unidade, a dezena, a centena e milhar!!