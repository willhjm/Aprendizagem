n = c = 0
while True:
    n = int(input('''-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Digite o número que deseja a tabuada
ou digite um número negativo para parar:  '''))
    if n < 0:
        break
    for c in range(0, 11):
        r = c * n
        print(f'{n} x {c} = {r}\n', end='')
print('FIM')
