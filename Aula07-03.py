import os

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

resultado = num1 + num2
resultado1 = num1 - num2
resultado2 = num1 * num2
resultado3 = num1 / num2

print("Digite S para soma, N para Subtração, M para multiplicação e D para divisão: ")
opcao = input()[0]

os.system('cls')

print(f"Os numeros foram :", num1, "e ", num2)

def Opcao (char):

     if(char == 's' or char == 'S'):
          print(f"O resultado da soma é: ", resultado)   

     if(char == 'n' or char == 'N'):
          print(f"O resultado subtração é: ", resultado1)

     if(char == 'm' or char == 'M'):
          print(f"O resultado multiplicação é: ", resultado2)

     if(char == 'd' or char == 'D'):
          print(f"O resultado divisão é: ", resultado3)


Opcao(opcao)
          