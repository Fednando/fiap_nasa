notas_digitada = {}

s = "S"

while not s == "N":
    nome = input("Digite o nome do Aluno: ")
    nota = float(input("Digite a notas dos alunos : "))

    if nome in notas_digitada:
        notas_digitada[nome].append(nota)
    else:
        notas_digitada[nome] = [nota]

    notas_digitada[nome] = nota

    if len(notas_digitada) > 2 :
       s = input("Caso queira saber a média dos Alunos digita S : ")
       if s == "s":
        result = sum(notas_digitada.values()) / len(notas_digitada)
        print(f"Média dos alunos : {result:.2}")
        for chave, valor in notas_digitada.items():
            textoFinal = "Aluno aprovado"
            if valor < 7.5:
                textoFinal = "Aluno reprovado"
            print(f'Nome: {chave}, Nota: {valor}    : {textoFinal}')





