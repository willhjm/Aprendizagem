nome = str(input('Insira o seu nome:    ')).strip
print('Analisando o seu nome')
# print('Seu nome em letra maiuscula fica assim {}'.format(nome.upper()))
# print('seu nome em letra minúscula fica assim {}'.format(nome.lower()))
print('Seu nome contém {} letras'.format(len(nome)-nome.count(' ')))