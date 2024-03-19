def calcula_velocidade_media(distancia: float, tempo: float, unidade_medida: str = "Km/h"):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")

#calcula_velocidade_media(200, 3, "Km/h")


def x():
    a = 15
    b = 3
    c = a / b
    d = c / b
    print(type(c))
    print(type(d))


x()


def loopTeste():
    a = 10
    b = 50
    a = a + b
    if bool(a):
        a = b + 10
        print(a)
    b = 0
    print(b)

loopTeste()

