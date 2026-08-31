lista = ["Ichigo", "Kempachi", "Aizen", "Remy"]
lista[3] = "Rukia"
print(lista[1:])

for index, item in enumerate(lista):  # Get index and item together
    print(f'index: {index} - item: {item}')

print("Aizen" in lista)

v1, v2, v3, v4 = ["Goku", "Vegeta", "Krilin", "Freezer"]
print(v1,v2,v3,v4)