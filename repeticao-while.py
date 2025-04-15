#exemplo1
'''
x = 0
while x<=10:
    print(x)
    x = x + 1

#exemplo2
m = 5
n = 1
while m>2:
    n = n+2
    m = m-1
print(m,n)

#exemplo3
x = 3
y = 4
z = 0
while x < y:
    z = z + x
    x = x + 1
    print(x, y, z)
'''
'''
#exercicio1
contagem = int(input("Digite um número de 5 a 10:"))
if 5 <= contagem <=10:
    print("Contagem regressiva:")
    while contagem >= 0:
        print(contagem)
        contagem -= 1
else:
    print("Número inválido")
'''
'''
#exercicio2
contador = 0
maior_numero = 0
while contador < 5:
    num = int(input("DIgite um número:"))
    if num > maior_numero:
        maior_numero = num
    contador += 1
print("O maior número é:", maior_numero)
'''
'''
#exercicio3
contador = 1
fat = 1
num = int(input("Digite um número:"))
while contador <= num:
    fat = fat * contador
    contador +=1
print("O fatorial do numero é:", fat)
'''
'''
#exercicio4
tamanho = int(input("Quantos numeros tera na lista:"))
soma = 0
contador = 0
while contador < tamanho:
    num = float(input("Digite um numero:"))
    soma += num
    contador +=1
media = soma / tamanho
print("O valor da media é:", media)
'''
#exercicio5
'''
contagem = 0
menu = 0
while contagem < 100:

    print("Menu:")
    print("1- Somar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Sair")

    menu = int(input("Escolha uma opção:"))

    if menu == 5:
        print("Operação finalizada")
        break
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite um número:"))


    if menu == 1:
        resultado = num1 + num2
        print(resultado)
        contagem += 1
    elif menu == 2:
        resultado = num1 - num2
        print(resultado)
        contagem += 1
    elif menu == 3:
        resultado = num1 * num2
        print(resultado)
        contagem += 1
    elif menu == 4:
        resultado = num1 / num2
        print(resultado)
        contagem +=1
    else:
        print("Operação inválida")
'''
#exercicio6
