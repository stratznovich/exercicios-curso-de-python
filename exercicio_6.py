'''
Faça um programa que leia 10 inteiros e imprima sua média
'''

contador = 1
soma = 0
saida = ''

while contador < 11:
    entrada = input('insira um valor ou digite "sair" para sair! ')
    if entrada == 'sair':
        print('o calculo foi encerrado! ')    
        break
    
    soma = soma + int(entrada)
    soma2 = soma / 10
    contador += 1
    if contador >= 11:
        print(f'valor total: {soma[0,1000]}')
        print(f'media: {soma2}')


