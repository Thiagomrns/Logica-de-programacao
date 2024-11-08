"""
***************************************************************************
No código abaixo, está contido o exercício de número 8 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    Solicite ao usuário do programa o seu peso e a altura. Calcule o 
    Índice de Massa Corporal (IMC) e classifique o resultado em: Abaixo 
    do peso (<18,5); Peso normal (18,5<=imc<24,9); sobrepeso (25<= imc< 29,9);
    obesidade>29,9. O imc = peso/altura^2
"""

# EXERCÍCIO 8: Cálculo de IMC

print(f"{'*' * 18}\n{'Cálculo de IMC'}\n{'*' * 18}")

h = float(input("Informe sua altura (em metros): "))
p = float(input("Informe seu peso (em quilos): "))
imc = p / (h**2)

if (imc < 18.5):
    print("De acordo com seu IMC, você está abaixo do peso.")
elif (imc >= 18.5 and imc <= 24.9):
    print("De acordo com seu IMC, você está no peso ideal.")
elif (imc >= 25 and imc <= 29.9):
    print("De acordo com seu IMC, você está classificado como sobrepeso.")
else:
    print("De acordo com seu IMC, você está na classificação de obesidade.")