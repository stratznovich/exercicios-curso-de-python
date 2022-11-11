'''
Escreva um programa que declare um inteiro, iricialize-o com O, e incremente-o de 1000
em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 mil).
'''

entrada = int(input('insira ym valor: '))
limite = 100000
while entrada < limite:
    print(entrada)
    entrada += 1000
    