print("Transformando temperatura de °F em °C")
tempF = float(input("Informe a temperatura em graus Fahrenheit:  "))
tempC = round(5 * ((tempF-32) / 9), 1)
print("A temperatura em graus Celsius é : " + str(tempC))