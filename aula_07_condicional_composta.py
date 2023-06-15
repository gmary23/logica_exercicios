"""
Faça um programa que fale se o número é par ou ímpar
"""
numero = int(input('Digite um número: '))


if numero % 2 == 0:
    print(f'O {numero} é par.')
else: 
    print(f'O {numero} é ímpar.')