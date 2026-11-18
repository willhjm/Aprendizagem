lista = list()
maior = menor = 0
pos = 0
for c in range(0, 5):
    num = int(input(f'Digite {c + 1}º valor: '))
    lista.append(num)
    if num > maior:
        maior = num
    else:
        menor = num
print(f'Os números digitados foram {lista}')
print(f'O maior número digitado foi {maior} na posição', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i +1}')
print(f'E o menor número digitado foi {menor} na posição', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i +1}')
