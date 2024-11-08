"""
***************************************************************************
No código abaixo, está contido o exercício de número 4 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    O programa deve solicitar um número e verificar se ele está dentro do
    intervalo de 1 a 100.   
"""

# EXERCÍCIO 4: Está no intervalo 1 - 100?
    
num = int(input("Digite um número inteiro: "))
if(num >= 1 and num <= 100):
    print("Sim, está no intervalo.")
else:
    print("Não está no intervalo.")