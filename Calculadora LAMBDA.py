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

    soma = lambda n1,n2:print(n1+n2)
    sub = lambda n1,n2:print(n1-n2)
    div = lambda n1,n2:print(n1/n2) 
    divint= lambda n1,n2: print(n1//n2)
    mult = lambda n1,n2:print(n1*n2)
    pot = lambda n1,n2:print(n1**n2)
    rq = lambda n1,n2:print (n1**(1/n2))

    op = input('Qual a operação deseja fazer?''\n'' '
    '\n''Soma = +''\n''Subtração = -''\n''Divisão = /''\n''Divisão Inteira = //'
    '\n''Multiplicação = x''\n''Potência = ^''\n''Raíz Quadrada = rq''\n'' '
    '\n''Digite aqui: ')
    
    import os 
    os.system('cls')
    
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
        rq(n1,n2)

    else:
        print('Operação inválida')