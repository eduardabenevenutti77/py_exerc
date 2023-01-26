#sorteio de nomes
import random
name1 = input('digite o nome do primeiro aluno:')
name2 = input('digite o nome do segundo aluno:')
name3 = input('digite o nome do terceiro aluno:')
name4 = input('digite o nome do quarto aluno:')

lista = [name1, name2, name3, name4]
#criação de uma variavel lista
sorteio = random.choice(lista)
#o choice ira sortear

print('o/a aluno/a {} irá apagar o quadro'.format(sorteio))

#sorteio apresentação
import random
g1 = str(input('quais são os participantes do grupo 1?'))
g2 = str(input('quais são os participantes do grupo 2?'))
g3 = str(input('quais são os participantes do grupo 3?'))
g4 = str(input('quais são os participantes do grupo 4?'))

list = [g1, g2, g3, g4]
sorteio = random.shuffle(list)
#shuffle embaralha

print('o primeiro grupo a apresentar é :')
print(list)