

# r -> solo lectura, w -> escritura , a (append)
# archivo_personas = open("no_existe.csv", "r")
"""archivo_personas = open("no_existe.csv", "a")

archivo_personas.write("asd\n")
archivo_personas.write("coasdasdmo\n")
archivo_personas.write("asdasd")

archivo_personas.close()
"""
with open("no_existe.csv", "r") as archivo:
    for linea in archivo:
        # print(linea, end="")
        print(linea.replace("\n", ""))

