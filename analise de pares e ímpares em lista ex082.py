lista = list()
r = 'S'
while r == 'S':
    num = int(input('Digite um valor: '))
    lista.append(num)
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r == 'N':
        break
print(f'Os números pares digitados foram {lista}')
