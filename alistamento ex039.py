from datetime import date
hoje = date.today().year

idade = int(input('Insira o ano que nasceu:  '))
ano = hoje - idade
prazo = 17 - ano

if ano == 17:
    print('Hora de se alistar')
elif ano < 17:
    print('Ainda não é hora de se alistar, faltam {} anos'.format(prazo))
elif ano > 17:
    prazo = prazo * -1
    print('Já passou da hora de se alistar, passou {} anos'.format(prazo))
