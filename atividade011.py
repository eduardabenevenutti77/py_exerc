
usu = str(input('Digite a sua cidade natal: ')).strip()
print(usu[:5].capitalize() == 'Santo')
#vefica se a str informada pelo usuário tem 5 letras e se é igual a santos
#strip tira os espaços
#capitalize deixa a primeira letra maiuscula e resto minusculo

usu1 = str(input('Digite o seu sobrenome: ')).strip()
#print(usu1[:5].capitalize() == 'Silva')
#print(usu1.find('Silva'))
print('seu nome tem Silva? {}'.format('Silva' in usu1))
#vefica se tem silva no usu1
