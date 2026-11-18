lista = list()
r = 'S'
cont = 0
while r == "S":
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont += 1
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r == 'N':
        if 5 in lista:
            print(f'Contém o número 5 na sua lista')
        else:
            print(f'Não contém o número 5 na sua lista')
        lista.sort(reverse=True)
        break
print(f'Os valores na lista são {lista}')
print(f'Foram digitados {cont} valores na lista')

