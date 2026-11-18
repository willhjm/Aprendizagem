from time import sleep

fim = 0
while fim != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if fim == 4:
        fim = 5
    sel = 0
    while sel != 4:
        sel = int(input('''
        =================
        O que deseja fazer?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] novos números
        [5] Sair
        =================   '''))
        if sel == 1:
            soma = valor1 + valor2
            print(f'A soma de {valor1} com {valor2} é {soma}\n')
        elif sel == 2:
            soma = valor1 * valor2
            print(f'{valor1} x {valor2} = {soma}\n')
        elif sel == 3:
            if valor1 > valor2:
                print(f'O número {valor1} é maior que {valor2}\n')
            elif valor1 == valor2:
                print('Os valores são iguais\n')
            else:
                print(F'O número {valor2} é maior que {valor1}\n')
        elif sel == 5:
            sel = 4
            fim = 5
            print('Finalizando...\n')
        sleep(2)
sleep(1)
print('Fim do programa')
