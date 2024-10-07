encabezado = None

todas_las_personas = []

def todo_es_un_numerico(valor):
    return valor.isnumeric()

with open("personas.csv", "r", encoding='utf-8') as archivo:
    for pos, linea in enumerate(archivo):

        persona_raw = linea.replace("\n", "")
        if pos == 0:
            encabezado = persona_raw.split(";")
            continue
        persona = persona_raw.split(";")
        persona_dict = {titulo: persona[index] for index, titulo in enumerate(encabezado)}

        if todo_es_un_numerico(persona_dict["dni"]):
            todas_las_personas.append(persona_dict)

print("Lista de personas:", todas_las_personas)