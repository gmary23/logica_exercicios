ano_atual = int(input('Em que ano estamos? '))
ano_nasc = int(input('Em que ano você nasceu? '))

idade = ano_atual - ano_nasc
print()
if idade >= 18:
    print(f'Você tem {idade} anos e já está na maioridade.')
else:
    print(f'Você tem {idade} anos e ainda é menor de idade.')

