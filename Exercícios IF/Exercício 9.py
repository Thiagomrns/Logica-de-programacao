"""
***************************************************************************
No código abaixo, está contido o exercício de número 9 do slide disponibi-
lizado pela professora.
***************************************************************************

Realizado em casa

Exercício:
    Solicite uma nota ao usuário e determine se o aluno foi aprovado,
    recuperação (5 a 7) ou reprovado (<5), com base em uma nota de corte.
    Nota de corte 7.
"""


# EXERCÍCIO 9: Aprovado ou reprovado com base numa nota de corte

print(f"{'*' * 18}\n{' Cálculo de média'}\n{'*' * 18}")

nota = float(input("Informe sua nota: "))

if (nota < 5):
    print("Você está reprovado.")
elif (nota >= 7):
    print("Você está aprovado.")
else:
    print("Você ficou de recuperação.")