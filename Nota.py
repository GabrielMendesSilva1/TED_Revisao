print(" Verificar valor  ")
nota = float(input("Digite um numero de 0 a 10: "))
while (nota > 10) or (nota < 0):
    nota = float(input("Valor invalido. Digite um numero de 0 a 10: "))
else:
    print("Nota informada: " + str(nota))