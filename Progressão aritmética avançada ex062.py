primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        cont += 1
        print('{} - '.format(termo), end=' ')
    print('PAUSA')
    mais = int(input('\nQuantos termos deseja a mais deseja mostrar? '))
print('Fim')
