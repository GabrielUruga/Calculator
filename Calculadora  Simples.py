# Calculadora simples 

'''
1. Boas vindas 
2. Inserir e armazenar primeiro valor
3. Inserir e armazenar segundo valor
4. Inserir qual a operação será realizada
5. Exibir o resultado da operação
'''
entrada = input ('Seja bem vindo à Calculadora Simples\n\nPressione ENTER para continuar: ')

if entrada != '':
    print('Você não inicializou a calculadora')
   
else: 
    import os
    os.system ('cls')
    
    n1 = float(input('Qual o primeiro valor? '))
    import os
    os.system ('cls')

    n2 = float(input('Qual o segundo valor? '))
    import os
    os.system ('cls')

    operation = input('SOMA = Digite Somar\nSUBTRAÇÃO = Digite Subtrair\nDIVISÃO = Digite Dividir\nMULTIPLICAÇÃO = Digite Multiplicar\n\nQual a operação que deseja fazer?\nDigite aqui: ')
    op = operation.capitalize()
    import os
    os.system ('cls')

    if op == 'Somar':
        soma = (n1+n2)
        print(f'Ao {op} {n1} e {n2} temos: {soma:.2f}')

    elif op == 'Subtrair':
        sub = n1-n2
        print(f'Ao {op} {n1} e {n2} temos: {sub:.2f}')

    elif op == 'Dividir':
        if n2 != 0:
            div = n1/n2
            print(f'Ao {op} {n1} e {n2} temos: {div:.2f}')
        else:
            print('Não é possível dividir um número por 0')

    elif op == 'Multiplicar':
        mult = n1*n2
        print(f'Ao {op} {n1} e {n2} temos: {mult:.2f}')

    else:
        print('Você não selecionou uma operação')