"""
***************************************************************************
No código abaixo, está contido o exercício de número 7 do slide disponibi-
lizado pela professora.
***************************************************************************

# -*- coding: utf-8 -*-

Created on Wed Oct 30 14:31:41 2024

@author: Aluno

Exercício:
    Desenvolva um programa que solicita um ano para o usuário e verifique 
    se ele é bissexto ou não.
"""

# EXERCÍCIO 7: O ano é bissexto?

# - Para saber se um ano é bissexto, basta verificar se é divisível por 4.

# - Anos centenários, como 1900, a regra é que o ano seja divisível por
# 400 para que o mês de fevereiro tenha um dia a mais.

ano = int(input("Digite o ano: "))

if(ano % 100 != 0 and ano % 4 ==0):
  #Se o ano não for divisível por 100 e for divisível por 4, é um ano bissexto.
    print(f"{ano} é um ano bissexto.")
elif(ano % 100 == 0 and ano % 400 ==0):  
  #Se o ano for divisível por 100 e for divisível por 400, é um ano bissexto.
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")