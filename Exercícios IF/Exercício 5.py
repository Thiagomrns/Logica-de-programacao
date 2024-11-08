"""
***************************************************************************
No código abaixo, está contido o exercício de número 5 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    O programa deve verificar se a idade de uma pessoa é suficiente para
    dirigir (18 anos ou mais).  
"""

# EXERCÍCIO 5: Pode dirigir?

idade = int(input("Digite sua idade: "))
if(idade >= 18):
    print("Você tem idade suficiente para dirigir.")
else:
    print("Você não possui idade suficiente para dirigir.")