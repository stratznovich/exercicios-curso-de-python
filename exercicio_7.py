'''
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média.
'''


funcao = 1
soma = 0
while funcao <= 10:
    entrada = int(input('insira 10 valores inteiros: '))
    if entrada <= 0:
        print('valores negativos sao invalido: ')
        print('tente novamente: ')
    soma = soma + entrada
    soma2 = soma / 10
    funcao = funcao + 1
    if funcao >= 11:
        print(f'resultado da sua media: {soma2}')





        


    
        




    





