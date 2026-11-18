import random
from random import randint
n = menor = maior = cont = 0
n = [random.randint(1, 10) for n in range(5)]
print(n)
cont += 1
if cont == 1:
    maior = menor = n
else:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    print(f'''O maior número sorteado foi {maior} e o menor foi {menor}''')