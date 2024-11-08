"""
***************************************************************************
No código abaixo, está contido o exercício de número 3 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    Desenvolva um programa onde o usuário entra com um número, e o programa
    verifica se ele é par ou ímpar.
"""
# EXERCÍCIO 3: O número é par ou ímpar?

num = int(input("Digite um número inteiro: "))
if(num % 2 == 0):
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")