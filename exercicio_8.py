'''
Escreva um programa que leia 10 números e escreva o mernr valor lido e o maior valor
lido.
'''

entrada = 0 
for numero in range(1, 11):
    entrada = int(input(f'insira 10 valores {numero}: '))
    if numero == 1:
        menor = entrada
        maior = entrada
    if entrada < menor:
        menor = entrada
    elif entrada > maior:
        maior = entrada

print(f'maior valor: {maior}, menor valor: {menor}')















        
