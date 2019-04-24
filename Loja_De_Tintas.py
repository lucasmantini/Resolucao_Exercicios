'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanho = float(input("Informe a área a ser pintada: "))
litros = int(tamanho/3)
latas = int(litros/18)

print(f"Número de latas necessárias: {latas}")
print(f"Total a ser pago: {latas*80}")
