#Ex1
ano = int(input("Digite o ano:"))
if ano%4 == 0:
    print("Esse ano é bissexto")
else:
    print("Não é ano bissexto")



#Ex2
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura(m):"))
imc = peso/(altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 18.5 < 24.9:
    print("Normal")
elif imc <=25 < 29.9:
    print("Sobrepeso")
elif imc <=30 < 34.9:
    print("Obesidade")
elif imc <=35 < 39.9:
    print("Obesidade mórbida")
else:
    print("Obesidade mórbida")



#Ex3
quantidade_produtos = int(input("Digite a quantidade de produtos:"))
valor_unidade = float(input("Digite o valor de cada unidade:"))

if  quantidade_produtos > 100:
    desconto = 0.1
else:
    desconto = 0.05

valor_desconto = valor_unidade * desconto
valor_desconto_unidade = valor_unidade - valor_desconto
valor_final = valor_desconto_unidade * quantidade_produtos

print("Resumo da compra:")
print("O valor inicial do produto é:", valor_unidade)
print("A quantidade de produtos é:", quantidade_produtos)
print("O desconto por unidade é:", valor_desconto_unidade)
print("O valor final com o desconto será:", valor_final)


#Ex4
idade = int(input("Informe sua idade:"))

if  18 <= idade < 70:
    print("Voto obrigatório")
elif 16 <= idade <18 or idade >70:
    print("Voto facultativo")
else:
    print("Não eleitor")


#Ex5
idade1 = int(input("Informe sua idade:"))
idade2 = int(input("Informe sua idade:"))
idade3 = int(input("Informe sua idade:"))


if idade1 == idade2 == idade3:
    print("As idades são iguais.")
else:

    maior_idade = idade1
    menor_idade = idade1

    if idade2 > maior_idade:
        maior_idade = idade2
    if idade3 > maior_idade:
        maior_idade = idade3


    if idade2 < menor_idade:
        menor_idade = idade2
    if idade3 < menor_idade:
        menor_idade = idade3


    print(f"A maior idade é: {maior_idade}")
    print(f"A menor idade é: {menor_idade}")


#Ex6
hora = int(input("Informe a hora:"))
minutos = int(input("Informe os minutos:"))
segundos = int(input("Informe os segundos:"))

if hora < 24 and minutos < 60 and segundos < 60:
    print("A hora é válida.")
else:
    print("A hora é inválida.")


#Ex7
nota = float(input("Digite sua nota:"))

if 9 <= nota <= 10:
    print("Sua nota é A")
elif 7 <= nota < 9:
    print("Sua nota é B")
elif 5 <= nota < 7:
    print("Sua nota é C")
elif 3 <= nota < 5:
    print("Sua nota é D")
elif 0 <= nota < 3:
    print("Sua nota é E")
else:
    print("Nota inválida.")


#Ex8
lado1 = float(input("Informe o primeiro lado:"))
lado2 = float(input("Informe o segundo lado:"))
lado3 = float(input("Informe o terceiro lado:"))
lado4 = float(input("Informe o quarto lado:"))

if lado1 == lado2 == lado3 == lado4:
    print("É um quadrado")
elif lado1 == lado3 and lado2 == lado4:
    print("É um retângulo")
else:
    print("Nenhum dos dois")


#Ex9
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
operacao = str(input("Digite a operação que deseja realizar(*, /, +, -):"))
if operacao == "+":
    resultado = numero1 + numero2
    print("O resultado é:", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("O resultado é:", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado é:", resultado)
elif operacao == "/":
    resultado = numero1 / numero2
    print("O resultado é:", resultado)
else:
    print("Operação inválida")


#Ex10
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

if nota1 <= nota2 and nota1 <= nota3:
    menor_nota = nota1
elif nota2 <= nota1 and nota2 <= nota3:
    menor_nota = nota2
else:
    menor_nota = nota3

if menor_nota == nota1:
    media = (nota2 + nota3) / 2
elif menor_nota == nota2:
    media = (nota1 + nota3) / 2
else:
    media = (nota1 + nota2) / 2

print("A média calculada (descontando a menor nota) é:", media)


#Desafio
import random

numero_secreto = random.randint(1, 10)

tentativa1 = int(input("Tente adivinhar o número (entre 1 e 10): "))

if tentativa1 == numero_secreto:
    print("Parabéns! Você acertou de primeira!")
elif tentativa1 > numero_secreto:
    print("Errou! O número é menor.")
else:
    print("Errou! O número é maior.")

# Segunda tentativa
tentativa2 = int(input("Tente novamente: "))

if tentativa2 == numero_secreto:
    print("Parabéns! Você acertou!")
elif tentativa2 > numero_secreto:
    print("Errou! O número era", numero_secreto)
else:
    print(f"Errou! O número era", numero_secreto)

