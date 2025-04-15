#exercicio1
'''
contador = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 3 == 0:
        contador += 1

print(f"\nVocê digitou {contador} número(s) que são múltiplos de 3.")
'''
#exercicio2
'''
while True:
    senha = "1234"
    tentativa = input("Digite a senha:")
    if tentativa == senha:
        print("Acesso concedido")
        break
    else:
        print("Senha incorreta. Tente novamente.")
'''
#exercicio3
'''
while True:
    print("Menu de Sobremesas")
    print("1- Bolo de Chocolate")
    print("2- Torta de Maracujá")
    print("3- Pavê de Limão")
    print("4- Pudim")
    print("5- Sair")

    menu = int(input("Escolha um número do menu:"))
    if menu == 1:
        print("Você escolheu Bolo de Chocolate.\n")
    elif menu == 2:
        print("Você escolheu Torta de Maracujá.\n")
    elif menu == 3:
        print("Você escolheu Pavê de Limão.\n")
    elif menu == 4:
        print("Você escolheu Pudim.\n")
    elif menu == 5:
        print("Fim da operação.")
        break
    else:
        print("Escolha inválida. Tente novamente.\n")

#exercicio4
'''
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo numero:"))

if num1 > num2:
    num1, num2 = num2, num1

for primos in range(num1, num2 + 1):
    if primos <= 1:
        continue
    for i in range(2, primos):
        if primos % i == 0:
            break
    else:
        print(f"Os números primos são: {primos}")

#exercicio5
'''
senha_correta = "2007"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha:")

    if senha == senha_correta:
        print("Senha correta.")
        break
    else:
        print("Senha incorreta.")
        tentativas += 1

if tentativas == 3:
    print("Fim das tentativas.")
'''
#exercicio6
'''
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite o um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:",pares)
print("Numeros impares:",impares)
'''
#exercicio7
'''
a = e= i = o = u = 0
frase = input("Digite uma frase:").lower()
for letra in frase:
    if letra == "a":
        a +=1
    elif letra == "e":
        e +=1
    elif letra == "i":
        i +=1
    elif letra == "o":
        o +=1
    elif letra == "u":
        u +=1
        
print(f"A frase possui: \n{a} letra a \n{e} letra e \n{i} letra i \n{o} letra o \n{u} letra u")
'''
#exercicio8
'''
import random
import time

cara = 0
while cara < 3:
    sorteio = random.choice(["cara", "coroa"])
    print(sorteio)
    if sorteio == "cara":
        cara +=1
    else:
        cara = 0

    time.sleep(1)
    
print("Fim")
'''
#exercicio9
'''
lista = []
quantidade = int(input("Quantos números terá na lista?"))
for i in range(quantidade):
    numero = int(input("Digite o um número: "))
    lista.append(numero)

media = sum(lista) / quantidade
menores = 0

for num in lista:
    if num <media:
        menores += 1

print(f"A média dos números é: {media}")
print(f"{menores} números são menores que a média")
'''
#exercicio10
'''
quantidade = int(input("Quantos números você vai digitar? "))

maior = segundo_maior = 0

for i in range(quantidade):
    numero = float(input(f"Digite o {i + 1}º número: "))

    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

if segundo_maior == 0:
    print("Não foi possível determinar o segundo maior número (todos são iguais ou só foi digitado um número).")
else:
    print(f"O segundo maior número é: {segundo_maior}")
'''