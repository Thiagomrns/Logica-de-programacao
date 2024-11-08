"""
***************************************************************************
No código abaixo, está contido o exercício de número 6 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    Desenvolva um programa que verifica o valor da compra e aplica um 
    desconto de 10% se o valor for maior que 100.   
"""

# EXERCÍCIO 6: Desconto de 10% se o preço for maior que 100

valor = float(input("Digite o valor da compra: "))
if( valor > 100 ):
    valor = valor * 0.9
    print(f"O valor com 10% de desconto fica: {valor}")
else:
    print("Nenhum desconto será aplicado ao valor da compra.")