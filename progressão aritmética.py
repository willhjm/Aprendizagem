print('Vamos fazer uma Progressão Aritmética (PA)')

primeiro = int(input('Digite o primeiro termo:    '))
razão = int(input('Digite a Razão:  '))
termo = primeiro + (10 - 1) * razão
c = 0

while primeiro in range(primeiro, termo, razão):
    print(f'{primeiro}', end=' - ')
print('Acabou')
