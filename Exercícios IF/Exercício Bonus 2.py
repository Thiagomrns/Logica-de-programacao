"""
***************************************************************************
No código abaixo, está contido o exercício bônus 2 do slide disponibilizado
pela professora.
***************************************************************************

Realizado em casa

Exercício:
    Escreva um programa para avaliar a concessão de uma bolsa de estudos com
    base na renda familiar e no desempenho acadêmico do aluno, conforme as regras
    abaixo:

1. Se a renda familiar for até R$ 2.000,00 e a nota média for 8.5 ou mais, o aluno
recebe uma bolsa integral.

2. Se a renda familiar for entre R$ 2.001,00 e R$ 4.000,00:
    1. O aluno recebe uma bolsa de 50% se sua nota média for 8.0 ou mais.
    2. O aluno recebe uma bolsa de 25% se sua nota média for entre 6.0 e 7.9.

3. Se a renda familiar for acima de R$ 4.000,00, o aluno não recebe bolsa
independentemente da nota.

O programa deve informar qual o percentual da bolsa (ou "nenhuma bolsa") com
base nos dados fornecidos.
"""

renda = float(input("Informe sua renda familiar: R$"))
media = float(input("Digite sua nota média: "))

if (renda <= 2000 and media >= 8.5): # Se a renda for até R$2000 e a média 8.5 ou maior
    print("Você pode receber uma bolsa integral!")

elif(renda >= 2001 and renda <= 4000): # Se a renda estiver entre R$2001 e R$4000
    if(media >= 8): # Se a média do aluno por 8 ou maior
        print("Você pode receber uma bolsa de 50%!")
    elif(media >= 6 and media <= 7.9): # Se a média estiver entre 6 e 7.9
        print("Você pode receber uma bolsa de 25%!")
    else:
        print("Você não tem direito a uma bolsa.")

else: # Se a renda for maior que R$4000, não tem direito a bolsa
    print("Você não tem direito a uma bolsa.")