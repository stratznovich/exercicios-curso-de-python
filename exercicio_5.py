'''
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
'''

'''
soma = 0
for i in range(10):
    entrada = int(input('insira um valor: '))
    soma = soma + entrada
print(soma)
'''

saida = ''
soma = 0
i = 1
while i < 11:
    entrada = input('insira um valor: ')
    if entrada == 'sair':
        print('conta encerrada')
        break
        
    soma = soma + int(entrada)
    i += 1
    if i >= 11:
        print(soma)


    


