from random import randint

print('=-' *20)
print('Vamos jogar Par ou Impar?')
print('=-' *20)

v= 0
while True:
    n = int(input('Escolha um valor: '))
    computador = randint(0, 10)
    total = n + computador
    q = ' '
    while q not in 'PI':
        q = str(input('Deseja par ou impar? ')).strip().upper()[0]
    print(f'Você jogou {n} e eu joguei {computador}. O total é {total} ', end='')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if q == 'P':
        if total % 2 == 0:
            v += 1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    elif q == 'I':
        if total % 2 == 1:
            v += 1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')
