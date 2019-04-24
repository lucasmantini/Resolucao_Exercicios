#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ('a', 'e', 'i', 'o', 'u')

letra = str.lower(input("Informe a letra: "))

if (letra in vogais):
    print('A letra é uma vogal!')
else:
    print('A letra é uma consoante!')
