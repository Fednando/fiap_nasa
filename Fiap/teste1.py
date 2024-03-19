numerorCrescente = [10, 1, 2, 3, 8, 5, 6, 7, 4, 9, 0]
listaAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

indexDec = 0
maior = 11
maiorAux = 1

# Primeiro for faz o loop para passar por todos os números 1 unica vezp
for indexDecrescente, valorDecrescente in enumerate(listaAux):
#   Segundo for vai passar varias vezes até encontrar o maior número e jogar na variavel maior.
#   Na primeiro fez a variavel maior recebera o valor 10, com isso as demais voltas não precisa passar todas as 10 vezes
#   diminuindo 1 numero a cada vez que passa.
    for indexCrescente, valorCrescente in enumerate(numerorCrescente):
        # verifica se o numero da lista é o maior encontrado e se é menor do que a variavel maior
        if valorCrescente > valorDecrescente and valorCrescente < maior:
            valorDecrescente = valorCrescente
            maiorAux = valorCrescente

    maior = maiorAux
    if indexDecrescente < len(listaAux) - 1:
        listaAux[indexDecrescente] = maior

print(f" Descrescente : {listaAux}")