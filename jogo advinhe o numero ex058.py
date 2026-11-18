import random
a = random.randint(0, 10)
r = 0
palpite = 0
acertou = False
print('Estou pensando em um número entre 1 a 10, tente advinhar')
while a != r:
    r = int(input('Qual é o número?    '))
    palpite += 1
    if a == r:
        acertou = True
    else:
        if a < r:
            print('Chute um pouco para menos')
        elif a > r:
            print('Chute um pouco para mais')
        else:
            print('O número está entre 1 e 10')
print('Acertou com {} tentativas'.format(palpite))
