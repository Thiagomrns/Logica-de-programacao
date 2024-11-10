"""
No código abaixo, está contido o início dos estudos sobre estruturas condicionais:
IF, ELIF e ELSE.

Para ver o código funcionando, selecione a parte desejada com o mouse e pressione
as teclas: CTRL + 1 (Spyder) ou CTRL + ; (VScode), para descomentar o código e o 
programa executa-lo.

 -*- coding: utf-8 -*-

Created on Wed Oct 23 14:47:26 2024

@author: Aluno
"""


# print("\nEste programa calcula a média aritmética entre 4 números.")

# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# n3 = float(input("Digite o terceiro número: "))
# n4 = float(input("Digite o quarto número: "))

# media_aritmetica = (n1 + n2 + n3 + n4) / 4

# print(f"\nA média aritmética entre {n1}, {n2}, {n3} e {n4} é {media_aritmetica}.")

# ....... IF e ELSE .......

print("\nEste programa calcula a média aritmética entre 4 números.")
# \n : Pula uma linha, a barra é invertida! \ invés de /

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

media_aritmetica = (n1 + n2 + n3 + n4) / 4

if (media_aritmetica < 6) :
    print("\nAluno em recuperação.\nSua média é: ", media_aritmetica)
else :
        print("\nAluno aprovado.\nSua média é: ", media_aritmetica)