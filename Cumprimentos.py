'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
#Código para corrigir o problema das letras minúsculas:
#turno = str.upper(input("Informe o turno que você estuda (M - matutino, V - vespertino ou N - noturno): "))

turno = input("Informe o turno que você estuda (M - matutino, V - vespertino ou N - noturno): ")

if (turno == 'M'):
    print("Bom-dia!")
elif (turno == 'V'):
    print("Boa-tarde!")
elif(turno == 'N'):
    print("Boa-noite!")
else:
    print("Valor inválido!")
