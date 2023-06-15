"""
Faça um programa onde na realização de um emprestimo tenha o 
juros no valor de 20%
"""
valor = float(input('Qual valor do emprestimo? '))
parcelas = int(input('Quer dividir em quantas parcelas? '))

emprestimo =  valor + (valor * 20)/100
resultado = emprestimo/parcelas

print(f'O valor do emprestimo fica {emprestimo}')
print(f'O valor de cada parcela será {resultado}')

