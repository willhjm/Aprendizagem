soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input(f'Digite o {c} valor:    '))
    if numero % 2 == 0:
        soma = soma + numero
        cont += 1
print(f'''Você informou {cont} números pares
      e a soma deles foi {soma}''')