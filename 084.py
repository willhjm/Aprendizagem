cont = 0
maior = menor = 0
temp = []
lista = list()
while True:
    temp.append(str(input('Digte o nome:   ')))
    temp.append(float(input('Qual o peso?    ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    cont += 1
    resp = str(input('Quer continuar? [S/N]    ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso foi de {maior} Kg')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} foi o maior peso')
print(f'O menor peso foi de {menor} Kg')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} foi o menor peso')
