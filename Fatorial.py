#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

controle = False

while(controle == False):
    fat = int(input("Informe um número para o calculo do fatorial: "))
    
    if (0 > fat):
        print("Número inválido! Não existe fatorial de números negativos, favor informar novo número!")
    else:
        controle = True

if (0 <= fat <= 1):
    print(f"Fatorial de {fat}= 1")
else:
    for i in range (1, fat):
        fat = fat * i

print(fat)
