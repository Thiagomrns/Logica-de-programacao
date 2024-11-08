"""
***************************************************************************
No código abaixo, está contido o exercício de número 1 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    Deve-se solicitar um número ao usuário e verificar se ele é positivo
    ou negativo.
"""

# EXERCÍCIO 1: O número é positivo ou negativo?

num = float(input("Digite um número: "))
if(num > 0):
    print(str(num) + " é um número positivo.")
else:
    print(str(num) + " é um número negativo.")