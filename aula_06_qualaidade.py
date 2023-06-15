"""
Escreva um programa que diga qual sua idade baseado no ano que estamos
"""

ano_atual = int(input('Em que ano estamos? '))
ano_nasc = int(input('Em que ano você nasceu? '))

idade = ano_atual - ano_nasc

print(f'Você tem {idade} anos.')