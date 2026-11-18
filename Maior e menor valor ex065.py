r = 'S'
cont = soma = media = maior = menor = 0
while r in "Ss":
    n = int(input('''Digite um número   '''))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('''Quer continuar? [S/N]    ''')).upper().strip()[0]
media = soma / cont
print(f'''-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Foram {cont} números
A soma dos valores é {soma}
O menor número é {menor} e o maior é {maior}
E a média dos números {media}''')
