"""
No código abaixo, está contido estudos ainda mais aprofundados sobre estruturas
condicionais e início de estudos sobre a estrutura de repetição WHILE

Para ver o código funcionando, selecione a parte desejada com o mouse e pressione
as teclas: CTRL + 1 (Spyder) ou CTRL + ; (VScode), para descomentar o código e o 
programa executa-lo.

# -*- coding: utf-8 -*-

Created on Wed Nov  6 13:35:37 2024

@author: Aluno
"""

#////////////////////////////////////////////////////////////////////////

# numeroCamisas = int(input("Número de camisas: "))
# valorCamisa= 12.50
# valorFinal = numeroCamisas * valorCamisa

# if(numeroCamisas <= 5) :
#     valorFinal = valorFinal * (1 - 3 / 100)
# elif(numeroCamisas <= 10) :
#     valorFinal = valorFinal * (1 - 5 / 100)
# else:
#     valorFinal = valorFinal * (1 - 7 / 100)

# print(f"Valor final: R${valorFinal:.2f}")

#////////////////////////////////////////////////////////////////////////


# Exercício 1 Grandezas elétricas

# print(f"{'*' * 20}\n{'GRANDEZAS ELÉTRICAS'}\n{'*' * 20}")
# print("1. Tensão (em Volt)")
# print("2. Resistência (em Ohm)")
# print("3. Corrente (em Ampére)")
# print("*" * 20)

# grandeza = int(input("Qual grandeza você deseja calcular? "))

# if(grandeza == 1):
#     print("Grandeza escolhida: Tensão.")
#     I1 = float(input("Forneça a corrente: "))
#     R1 = float(input("Forneça a resistência: "))
#     V1 = R1 * I1
#     print(f"A Tensão com {R1:.2f} Ohms e {I1:.2f} Ampéres é: {V1:.2f} Volts.")
# elif(grandeza == 2):
#     print("Grandeza escolhida: Resistência.")
#     I2 = float(input("Forneça a corrente: "))
#     V2 = float(input("Forneça a tensão: "))
#     R2 = V2 / I2
#     print(f"A resistênca com {V2:.2f} Volts e {I2:.2f} Ampéres é: {R2:.2f} Ohms.")
# elif(grandeza == 3):
#     print("Grandeza escolhida: Corrente.")
#     R3 = float(input("Forneça a resistência: "))
#     V3 = float(input("Forneça a tensão: "))
#     I3 = V3 / R3
#     print(f"A corrente com {V3:.2f} Volts e {R3:.2f} Ohms é: {I3:.2f} Ampéres.")
# else:
#     print("Você digitou uma opção inválida. Tente novamente.")
    
#////////////////////////////////////////////////////////////////////////

# Estruturas de repetição "Enquanto" (while)

# cont = 1

# while (cont <= 10):
#     print("Olá!")
#     cont += 1
# print("Fim.")

#////////////////////////////////////////////////////////////////////////

# soma = 0
# termo = 1

# while (termo <= 10):
#     soma += termo
#     termo += 1
# print(soma)

#////////////////////////////////////////////////////////////////////////