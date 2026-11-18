valor = int(input('Digite o valor que deseja saber o fatorial: '))
c = valor
fatorial = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else f' = {fatorial}', end='')
    fatorial *= c
    c -= 1
print(f'\nO fatorial de {valor} é {fatorial}')
print('fim')
