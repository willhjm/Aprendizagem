altura = float(input('Insira a altura em mt:  '))
peso = float(input('Insira o peso em Kg:    '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Abaixo do peso')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f}. Está ideal!')
elif imc <= 30.0:
    print(f'Seu IMC é {imc:.2f}. Está sobrepeso')
elif imc <= 40.0:
    print(f'Seu IMC é {imc:.2f}. Obesidade!')
elif imc > 40.0:
    print(f'Seu IMC é {imc:.2f}. Obesidade Mórbida!')