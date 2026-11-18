r = ' '
while r != 'M' and r != 'F':
    r = str(input('Qual o sexo? [M/F] ')).strip().upper()[0]
    if r != 'M' and r != 'F':
        print('Digite apenas M para masculino ou F para feminino')
print('Registrado com sucesso!')
