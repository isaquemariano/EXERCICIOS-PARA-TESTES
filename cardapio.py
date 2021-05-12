listagem = ('hamburguer', 4.99,
            'misto', 2.50,
            'pastel', 2.50,
            'coxinha', 2.50,
            'suco', 2,
            'refrigerante', 4,
            'sorvete', 2.00)
print('-'*40)
print(f'{"cardápio":^40}')
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2== 0:
        print (f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')