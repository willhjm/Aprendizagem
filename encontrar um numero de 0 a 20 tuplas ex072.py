p = ' '
while True:
    n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    p = int(input('Digite um número entre 0 e 20: '))
    if p >= 0 or p <= 20:
        print(n[p])
        break
