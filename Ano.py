ano = int(input("Digite um número correspondente a um ano e descubra se é bissexto: "))
if (ano% 4 == 0 and ano % 100 != 0) or (ano%400 == 0):
    print(" O ano", ano, "é um  bissexto")
else:
    print(ano, "não é um ano bissexto!")