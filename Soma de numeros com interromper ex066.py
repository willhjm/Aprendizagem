n = cont = soma = 0
while True:
    n = int(input('''Digite um número [Digite 999 para parar]:   '''))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'''-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Foram digitados {cont} valores
A soma entre eles é {soma}
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-''')