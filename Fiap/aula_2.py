listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaQuatroNum = [2, 3, 1, 4]
listaCincoNomes = ["Ana", "Paula", "Fernandes", "Sandro", "Paulo"]
listaString = ["A", "B", "C"]

# 8






numerorCrescente = [10, 1, 2, 3, 8, 5, 6, 7, 4, 9, 0]
listaAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

indexDec = 0
maior = 11
maiorAux = 1
for indexDecrescente, valorDecrescente in enumerate(listaAux):
    for indexCrescente, valorCrescente in enumerate(numerorCrescente):
        if valorCrescente > valorDecrescente and valorCrescente < maior:
            valorDecrescente = valorCrescente
            maiorAux = valorCrescente

    maior = maiorAux
    if indexDecrescente < len(listaAux) - 1:
        listaAux[indexDecrescente] = maior

print(f" Descrescente : {listaAux}")








# 1
soma = 0
for index, valor in enumerate(listaNumeros):
    soma = valor + soma

print(f"A soma é : {soma}")
print(f"A soma é fun sum : {sum(listaNumeros)}")

# 2
textComVirgula = ""
for index, texto in enumerate(listaString):
    if (index < len(listaString) - 1):
        textComVirgula += f"{texto},"
    else:
        textComVirgula += texto

print(f"Texto com virgula : {textComVirgula}")

# 3
maior = 0
for index, valor in enumerate(listaQuatroNum):
    if valor > maior:
        maior = valor
    print(f"Valor maior da lista : {maior}")

for index, texto in enumerate(listaString):
    print(f"Elementos de uma lista : {texto}")

# 4
for index, valor in enumerate(listaNumeros):
    if (valor % 2 == 0):
        print(f"Numero par : {valor}")
    else:
        print(f"Numero impar : {valor}")

    # 5 ?

# 6
aux = 10
while (aux > 1):
    aux -= 1
    print(aux)

    if aux == 1:
        print("Fogo!")

numeroPar = 1
while (not numeroPar % 2 == 0):
    numeroPar = int(input("Digite um numero: "))

    if numeroPar % 2 == 0:
        print(f"Voce digitou um numero par : {numeroPar}")
        break

numeroEscolhido = 1
tentativas = 1
numeroSorteado = 0  # random.randint(1, 10)
while (tentativas < 3):
    tentativas += 1
    numeroEscolhido = int(input("Tente adivinhar o numero : "))

    if numeroSorteado == numeroEscolhido:
        print("Voce acertou o numero")
        break

numeroPositivo = 0
while (numeroPositivo > 0):
    numeroPositivo += int(input("Digite numeros positivos : "))
    if numeroPositivo < 0:
        print(f"Total dos valores positivos foram : {numeroPositivo}")

multiplos = 3
contador = 0
resultado = 0
while (contador < 11):
    resultado = multiplos * contador
    contador + +1
    print(f"{contador} * {multiplos} = {resultado}")








