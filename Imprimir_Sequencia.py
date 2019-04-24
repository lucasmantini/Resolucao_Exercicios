'''
Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a 
n-ésima linha.
'''


def Imprimir_Sequencia(x):
    for i in range (x + 1):
        print(f"{i} " * i)

num_linhas = int(input("Informe o número de linhas totais: "))
Imprimir_Sequencia(num_linhas)   
