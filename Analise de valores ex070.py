soma = pm = pb = cont = 0
barato = ' '
while True:
    produto = str(input('Produto:  ')).strip().upper()
    preço = int(input('Preço:   '))
    cont += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    soma += preço
    if cont == 1 or preço < pb:
        pb = preço
        barato = produto
    if preço > 1000:
        pm += 1
    if r == 'N':
        print(f'Sua compra deu o total de R$ {soma:.2f}')
        print(f'Temos {pm} produtos custando mais de R$ 1000,00')
        print(f'O produto mais barato foi {barato} e custou R$ {pb:.2f} ')
        break