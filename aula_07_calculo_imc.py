"""
Faça um programa que calcule o IMC - índice de massa corporal
"""
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * 2)

if imc >= 18.5 and imc < 25:
    print(f'Parabéns! Seu imc é {imc} você está no seu peso ideal')
else:
    print(f'Seu imc é {imc} você não está na faixa de peso ideal')



