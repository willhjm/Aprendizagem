import stop

print('-=' *20)
print(f'{'''Padaria do William''':^40}')
print('-=' *20)

lista = ('café', 'R$ 0,50', 'pão de queijo', 'R$ 0,30', 'pão na chapa', 'R$ 3,50', 'misto quente', 'R$ 8,00', 'suco natural', 'R$ 8,00', 'garrafa de água', 'R$ 2,00')
for padaria in range(0, len(lista)):
    if padaria % 2 == 0:
        print(f'{lista[padaria]:.<33}', end='')
    else:
        print(f'{lista[padaria]}', end='\n')
r = str(input('''Aperte 'enter' para encerrar
'''))
if r == ' ':
    stop()