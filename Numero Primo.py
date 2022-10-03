print("  Verificando numeros primos  ")
numero = int(input("Digite um numero para saber todos os primos existentes menores que esse número "))

numero = int(input("Digite um número para saber os seus divisores primos: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, "Não é primo!")
            break
    else:
        print(numero, "É primo!")
elif numero == 0:
    print(numero, "É zero")
elif numero == 1:
    print(numero, "1 Não é numero primo!")
else:
    print(numero, " É negativo ")