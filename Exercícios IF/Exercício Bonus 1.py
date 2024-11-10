"""
***************************************************************************
No código abaixo, está contido o exercício bônus 1 do slide disponibilizado
pela professora.
***************************************************************************

Realizado em casa

Exercício:
    Escreva um programa que calcule o valor do frete de uma encomenda com
    base na distância e no peso fornecidos pelo usuário. As regras para 
    cálculo do frete são as seguintes:

1. Se o peso for até 2 kg, o valor do frete será:
    1. R$ 5,00 para até 100 km,
    2. R$ 8,00 para distâncias entre 101 km e 500 km,
    3. R$ 10,00 para distâncias maiores que 500 km.
2. Se o peso estiver entre 2 kg e 10 kg, o valor do frete será:
    1. R$ 10,00 para até 100 km,
    2. R$ 15,00 para distâncias entre 101 km e 500 km,
    3. R$ 20,00 para distâncias maiores que 500 km.
3. Para pesos acima de 10 kg, o valor do frete será:
    1. R$ 20,00 para até 100 km,
    2. R$ 30,00 para distâncias entre 101 km e 500 km,
    3. R$ 40,00 para distâncias maiores que 500 km.

    O programa deve calcular e exibir o valor do frete com base nas 
    informações fornecidas.
"""

# EXERCÍCIO BÔNUS 1: Valor do frete.

p = float(input("Informe o peso do seu produto (em Quilos): "))
d = float(input("Informe a distância até o destino (em Quilômetros): "))

# Se o peso for até 2 Kg :
if (p <= 2):
    if (d <= 100): # Se a distância for até 100 Km
        frete = 5.00
    elif (d >= 101 and d <= 500): # Se a distância estiver entre 100 Km e 500 Km
        frete = 8.00
    else: # Se a distância for maior que 500 Km
        frete = 10.00

# Se o peso estiver entre 2 Kg e 10 Kg :
elif (p > 2 and p <= 10):
    if (d <= 100):
        frete = 10.00
    elif (d >= 101 and d <= 500):
        frete = 15.00
    else:
        frete = 20.00

# Se o peso for maior que 10Kg :
else:
    if (d <= 100):
        frete = 20.00
    elif (d >= 101 and d <= 500):
        frete = 30.00
    else:
        frete = 40.00

print(f"O valor do frete será R${frete:.2f}") # .2f significa Duas casas decimais