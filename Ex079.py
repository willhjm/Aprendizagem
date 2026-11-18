r = 'S'
lista = list()
while r == 'S':
    num = int(input('Digite o valor númerio: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número duplicado, não cadastrado')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(sorted(lista))