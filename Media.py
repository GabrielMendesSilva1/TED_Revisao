
print("Calculando a média do aluno!")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota:  "))
nota3 = float(input("Insira a terceira nota:  "))

media = round((nota1 + nota2 + nota3) / 3, 1)

if media >= 7.0 and media < 10:
    print("Aprovado com média: " + str(media))
elif media >= 10:
    print("Aprovado com Distinção! Média: " + str(media))
else:
    print("Reprovado. Média:" + str(media))