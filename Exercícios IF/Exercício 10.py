"""
***************************************************************************
No código abaixo, está contido o exercício de número 10 do slide disponibi-
lizado pela professora.
***************************************************************************

Realizado em casa

Exercício:
    Solicite três números ao usuário e verifique qual deles é o maior.
    Aponte qual o maior número.
"""

# EXERCÍCIO 10: Qual número é maior?

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if (num1 >= num2 and num1 >= num3):
    print(f"O número {num1} é o maior número.")

elif (num2 >= num1 and num2 >= num3):
    print(f"O número {num2} é o maior número.")

else:
    print(f"O número {num3} é o maior número.")