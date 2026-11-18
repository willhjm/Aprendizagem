from time import sleep
print('-' *30)
print('{:^30}'.format('BANCO EVOL(UIU)'))
print('-' *30)

while True:
    valor = int(input('Qual o valor que você deseja sacar? R$ '))
    ced = 100
    total = valor
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} notas de R$ {ced}')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totced = 0
            if total == 0:
                break
    print('-' * 30)
    r = str(input('Deseja sacar outro valor? [S/N]  ')).strip().upper()[0]
    print('-' * 30)
    if r in 'N':
        break
print('=-' * 20)
print('{:^30}'.format('Volte sempre ao BANCO EVOL(UIU)!'))
print('=-' * 20)
sleep(4)