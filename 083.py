expr = str(input('Digite a sua expressão matemática: '))
if expr.count('(') == expr.count(')'):
    print('A sua expressão é válida')
else:
    print('Sua expressão está incorreta')
