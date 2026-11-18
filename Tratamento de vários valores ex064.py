n = cont = soma = 0
while n != 999:
    n = int(input('''Digite um número a ser somado [999 para cancelar]    '''))
    soma += n
    cont += 1
    if n == 999:
        print(f'''A soma dos {cont - 1} números foram {soma - 999}''')
print('FIM')