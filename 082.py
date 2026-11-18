lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
for i, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Pares: {pares}')
print(f'Impares: {impares}')
print('Sua lista é {}'.format(lista))
