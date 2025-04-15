'''
age = int(input("Qual sua idade?"))
if age < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

nota = float(input("Digite sua nota:"))
if nota >= 9.0:
    print("Excelente!")
elif nota >= 7.0  < 9.0:
    print("Boa!")
elif nota >= 5.0 <9.0:
    print("Média")
else:
    print("Insuficiente")

~~~~

x = int(input("Digite um numero:"))
if x%2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
if x%3 == 0:
    print("O número é múltiplo de 3")
if x%5 == 0:
    print("O número é múltiplo de 5")

~~~~

x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))

if x > y:
    print(x, "é o maior número")
elif y > x:
    print(y, "é o maior número")
else:
    print("Os números são iguais")

~~~~

x = int(input("Digite sua idade:"))

if x < 2:
    print("Sua classificação de idade é: bebê")
elif x<13:
    print("Sua classificação de idade é: criança")
elif x<18:
    print("Sua classificação de idade é: adolescente")
elif x<60:
    print("Sua classificação de idade é: adulto")
else:
    print("Sua classificação de idade é: idoso")

~~~~

print("Escolha a conversão que deseja fazer:")
print("1- Celsius para Fahrenheit")
print("2- Fahrenheit para Celsius")

uni = int(input("Digite 1 ou 2: "))

if uni == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
elif uni == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F é igual a {celsius}°C")
else:
    print("Número inválido")

~~~~

x = float(input("primeiro lado:"))
y = float(input("segundo lado:"))
z = float(input("terceiro lado:"))

if x + y > z and y + z > x and z + x > y:
    if x == y == z:
        print("O triângulo é equilátero")
    elif x != y != z:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Não forma um triângulo")
'''