def nombre() ->str:
    texto = ""
    for x in range(5):  #[0,1,2,3,4]
        texto += f"Carlos {x},"
    return texto

def datos():
    return "Carlos", 20


print(nombre())

nom, edad = datos()
print(nom, edad)