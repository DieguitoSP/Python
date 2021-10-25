import json
# Para codificar y escribir directamente usamos json.dump; podemos codificar todo tipo de dato
# Listas de diccionarios
videojuegos = [
    {
        "nombre": "Super Mario Bros 3",
        "consola": "NES",
    },
    {
        "nombre": "Halo Combat Evolved",
        "consola": "Xbox",
    },
    {
        "nombre": "Crash Team Racing",
        "consola": "PSX",
    },
]
# ¿Quieres escribirlo a un archivo? fácil:
with open("videojuegos.json", "w") as archivo:
    json.dump(videojuegos, archivo)

f= = open("videojuegos.json","r")
content = f.read()
jsondecoded = json.loads(content)
