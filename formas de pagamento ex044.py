valor_produto = float(input('Qual o valor do produto?   '))
forma_pagamento = int(input('''Qual a forma de pagamento?
                            Insira (0) para dinheiro
                            Insira (1) para cartão à vista
                            Insira (2) para parcelamento x2
                            Insira (3) para parcelamento x3
                            '''))

# Adicionar desconto ou juros conforme a forma de pagamento
desconto1 = valor_produto * 0.10
desconto2 = valor_produto * 0.05
juros = valor_produto * 1.20

if forma_pagamento == 0:
    valor_real = valor_produto - desconto1
    print(f'O produto sai pelo valor de {valor_real:.2f}')
elif forma_pagamento == 1:
    valor_real = valor_produto - desconto2
    print(f'O produto sai pelo valor de {valor_real:.2f}')
elif forma_pagamento == 2:
    print(f'O produto sai pelo valor de {valor_produto:.2f}')
elif forma_pagamento == 3:
    print(f'O produto sai pelo valor de {juros:.2F}')