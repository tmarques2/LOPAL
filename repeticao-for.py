'''
#lista
frutas = ['maçã', 'banana', "laranja", 'uva']
for fruta in frutas:
    print(fruta)
print(frutas[3])
'''
'''
#string
mensagem = 'Hello Word!'
for caractere in mensagem:
    print(caractere)
'''
'''
#tupla
cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print("Cor:", cor)
'''
'''
#dicionario
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "profissão": "engenheira"
}
print(pessoa["nome"])
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")
'''
'''
#dicionario dentro do dicionario
alunos = {
    "123": {
        "nome": "Lucas",
        "idade": 17},
    "456": {
        "nome": "Maria",
        "idade": 18}
}
print(alunos["456"]["nome"])
for ra, dados in alunos.items():
    print(f"RA:{ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")
'''
'''
#conjunto
animais = {"gato", "cachorro", "elefante", "girafa"}
for animal in animais:
    print("Animal:", animal)
'''
'''
#range
for numero in range(0,101,10):
    print(numero)
'''
'''
#arquivos
nome_arquivo = "C:/Users/49074251803/Documents/thai.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
'''
'''
#ex1
for numero in range(0,10,2):
    print(numero)
'''
'''
#ex2
cores = ["vermelho", "verde", "azul", "amarelo"]
for cor in cores:
    print("Cor:", cor)
'''
'''
#ex3
soma = 0
for numero in range(1,101):
    soma+=numero
print(soma)
'''
'''
#ex4
numero = int(input("Digite um número:"))
for i in range(1,11):
    tabuada = numero*i
    print(f"{numero} x {i} = {tabuada}")
'''
'''
#ex5
tamanho = int(input("Digite o tamanho da lista:"))
numeros = []
soma = 0
for _ in range(tamanho):
    num = float(input(f"Digite um número: "))
    numeros.append(num)
    soma += num

media = soma / tamanho
print(f"A média dos números é: {media}")
'''