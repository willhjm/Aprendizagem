print("Vamos analisar um triangulo?")

r1 = float(input('Insira o valor do primeiro lado:  '))
r2 = float(input('Insira o valor do segundo lado:   '))
r3 = float(input('Insira o valor do terceiro lado:  '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('É um triângulo ISÓSCELES!')
    else:
        print('É um triangulo ESCALENO!')
else:
    print('As retas não podem formar um triangulo!')