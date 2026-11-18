from datetime import date
ano1 = date.today().year

idade = int(input('insira o ano de nascimento:  '))
ano = ano1 - idade

if ano <= 9:
    print('Mirim')
elif ano <= 14:
    print('infantil')
elif ano <= 19:
    print('Junior')
elif ano <= 20:
    print('Sênior')
elif ano >= 21:
    print('Master')