'''
Escreva um programa que na tela, de I até 100, de I em I, 3 vezes.
a primeira usando o loop for 
a segunda e terceira usando o loop while.
'''

for numero in range(1, 101):
    print(numero, end=', ')


contagem = 1
while contagem < 101:
    print(contagem, end=', ')
    contagem += 1


contador = 0
while (contador < 101):
    print(contador)
    contador += 1
    if (contador == 101):
        break
print('fim do loop')


