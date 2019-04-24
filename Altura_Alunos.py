'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando 
o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

numero = [0]*10
altura = [0]*10
maxAlt = [-1, -1]
minAlt = [-1, 10000]

for i in range(0, 10):
    numero[i] = int(input("Informe o número do aluno: "))
    altura[i] = int(input("Informe a altura do aluno: "))

for i in range(0, 10):    
    if (maxAlt[1] < altura[i]):
        maxAlt = [numero[i], altura[i]]
    if (minAlt[1] > altura[i]):
        minAlt = [numero[i], altura[i]]

print("")
print(f"O aluno {maxAlt[0]} é o mais alto da turma: {maxAlt[1]}cm.")
print(f"O aluno {minAlt[0]} é o mais baixo da turma: {minAlt[1]}cm.")
