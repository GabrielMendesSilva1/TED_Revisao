print("Ivertendo ordem de numeros")
idades = []
alturas = []
for x in range(5):
    idades.append(int(input("Informe sua idade: ")))
    alturas.append(float(input("Informe sua altura: ")))

print("\n\nIdades informadas em ordem direta: " ,  idades)
print("Alturas informadas em ordem direta: " ,  alturas)
print("\n\nIdades em ordem inversa " , idades[::-1])
print("Alturas em ordem inversa " , alturas[::-1])