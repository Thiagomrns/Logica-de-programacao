"""
***************************************************************************
No código abaixo, está contido o estudo feito a respeito da função print e
operadores lógicos.
***************************************************************************
"""



# Comentário
print("Olá!") # Comentário 2

print("#Não é comentário!")
# É comentário também!

''' Teste comentários 
Primeira linha
Segunda linha
'''

# Imprimir o caractere aspas "
print("Desejo imprimir \" por algum motivo") 
# Imprimir o caractere barra \
print("Esse arquivo está em C\\:Disco_Local")

print("Isso\né\num\nexemplo.") # \n pula uma linha
print("Isso\té\n\tum\texemplo.") # \t é um Tab    

'''f-string admite variáveis no print'''
# print(f"Me chamo{nome} e tenho {idade} anos.") #

from math import pi # Importa pi da biblioteca de matemática
from math import tau, e # Importa tau e Euler da biblioteca de matemática
print(pi)
print(tau, e)

''' Caracteres: string ou str
Números inteiros: int ou integer
Números reais: float'''

numero_inteiro = 5  # int ou integer
numero_virgula = 9.69 # float
mensagem = "Olá" # string

x = int(input("Digite um número: ")) # converte os dados da variavel para int
y = x + 5
print(y) # type te retorna o tipo da função!

print(type(int(5)))
print(type(float(5)))
print(type(str(5)))

# função pow(base, exp) potenciação ou **
print(pow(4, 2))
print(4 ** 2)

x = 2 # x recebe 2
x += 2 # x recebe x + 2
print(x)
x -= 2 # x recebe x - 2
print(x)
x *= 2 # x recebe x * 2
print(x)
x /= 2 # x recebe x / 2
print(x)
x %= 2 # resto da divisão de x por 2
print(x)
x **= 2 # x recebe x elevado a 2
print(x)
x //= 2 # quociente da divisão de x
print(x)