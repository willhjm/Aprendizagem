from time import sleep
sexo = m = f = i = 0
while True:
    pessoa = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        sexo = m
        m += 1
    if sexo == 'F' and idade < 20:
        sexo = f
        f += 1
    if idade >= 18:
        idade = i
        i += 1
    print('-'*30)
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]  ')).strip().upper()[0]
    if r == 'N':
        sleep(1)
        print(f'São {i} maiores de 18 anos')
        print(f'São {m} homens cadastrados')
        print(f'São {f} mulheres com menos de 20 anos')
        break
print('Fim')