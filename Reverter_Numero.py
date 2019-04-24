'''
Reverso do número. 
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

def Reverter_Num (x):
    x = x[::-1]
    return x

num = input("Informe um número, preferencialmente um número com 2 algarismos ou mais, distintos: ")
print(Reverter_Num(num))