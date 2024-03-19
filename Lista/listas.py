from funcoes.teste_funcao import loopTeste

loopTeste()


lista = [12, 34.3, "Texto"]

lista.append("Teste de inserção")
print(lista)
print(lista[0:3])

for valor in lista:
    print(valor)

#removendo
lista.pop()
print("Remove" + str(lista))

#Tamanho
print(len(lista))

dic = {"nome" : "Fernando", "telefone" :  "12341234"}

for c, v in dic.items():
    print(f"{c} - {v}")

C = [10, 15, (44, 44)]
print(type(C))

for valor in range(0, 50, 1):
    print(valor)


def x():
    a = 15
    b = 5
    c = a + b
    while a < b:
        b = b + 1
    c = b + 2

    print(f"Valores  a e b {a} - {b} - {c}")

x()