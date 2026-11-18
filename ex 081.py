lista = list()
cont = 0
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Você digitou {cont} valores')
if 5 in lista:
    print('O valor 5 apareceu na lista')
else:
    print('O valor 5 não apareceu na lista')