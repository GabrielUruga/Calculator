print('Calculadora by Gabriel Uruga')
print(' ')
entrada = input('Pressione ENTER para continuar: ')

import os 
os.system('cls')

if entrada == '':
    import os 
    os.system('cls')

    n1 = int(input('Digite o primeiro valor: '))

    import os 
    os.system('cls')

    n2 = int(input('Digite o segundo valor: '))

    import os 
    os.system('cls')

def soma(n1,n2):
    somar =[n1,n2]
    print(sum(somar))

def sub(n1,n2):
    print(n1-n2)

def div(n1,n2):
    print(n1/n2)

def divint(n1,n2):
    print(f'{n1/n2:.0f}')

def mult(n1,n2):
    print(n1*n2)

def pot(n1,n2):
    print(n1**n2)
    
def root(n1,n2):
    print(f'{n1**(1/n2):.0f}')

    op = input('Qual a operação deseja fazer?''\n'' '
    '\n''Soma = +''\n''Subtração = -''\n''Divisão = /''\n''Divisão Inteira = //'
    '\n''Multiplicação = x''\n''Potência = ^''\n''Raíz Quadrada = rq''\n'' '
    '\n''Digite aqui: ')
    
    if op == '+':
        soma(n1,n2)

    elif op == '-':
        sub(n1,n2)  

    elif op == '/':
        div(n1,n2)

    elif op == '//':
        divint(n1,n2)

    elif op == 'x':
        mult(n1,n2)

    elif op == '^':
        pot(n1,n2)

    elif op == 'rq':
        root(n1,n2)
        
    else:
        print('Operação inválida') 