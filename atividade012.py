#analise uma string, mostre ao usuário a posição que ela aparece e última

frase = str(input("informe uma frase para o sistema fazer a analise: ")).upper().strip()
#UPPER -> CASO O USUÁRIO TENHA ESCRITO COM LETRA MINUSCULO, O SISTEMA TRANSFORMA PARA MAIUSCULO
print('a letra A aparece: {} vezes '.format(frase.count('A')))
#COUNT -> CONTA QUANTAS VEZES DETERMINADA LETRA APARECEU NA TELA
print('a primeira letra A apareceu na posição: {}'.format(frase.find('A')+1))
#FIND -> ACHA A LETRA NO MEU NA STRING E FALA A POSIÇÃO (a primeira posição é sempre 0)
print('a última letra A apareceu na posição: {}'.format(frase.rfind('A')))
#Rfind -> o sistema começa a procurar pelo lado direito
