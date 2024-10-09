import os
import re

# Directorio
ruta_carpeta = "D:\\Musica"

# Expresión regular
patron = re.compile(r'[^a-zA-Z\s]')

# Diccionario para nombres de archivo duplicados
nombres_existentes = {}

# Recorremos los archivos en la carpeta
for nombre_archivo in os.listdir(ruta_carpeta):
    # Renombrar solo si es un archivo (no una carpeta)
    if os.path.isfile(os.path.join(ruta_carpeta, nombre_archivo)):
        # todo a minúsculas desde el principio
        nombre_archivo = nombre_archivo.lower()

        nuevo_nombre = re.sub(r'^ymatecom', '', nombre_archivo) #(yt5s.io - , r'^ymate\.com')
        # Limpiando aun mas el nombre
        nuevo_nombre = re.sub(r'[0-9]', '', nuevo_nombre)
        nuevo_nombre = re.sub(patron, '', nuevo_nombre).strip()
        nuevo_nombre = re.sub(r'\s+', ' ', nuevo_nombre)  # Reducir múltiples espacios a uno

        nuevo_nombre = nuevo_nombre.replace('mp', '')  # Eliminar 'mp' en cualquier lugar del nombre

        # solo un ".mp3" al final
        nuevo_nombre = re.sub(r'\.+mp3$', '.mp3', nuevo_nombre)  # Si hay ".mp3", se asegura de que sea solo una vez.
        nuevo_nombre = re.sub(r'(\.mp)+$', '.mp3', nuevo_nombre)  # Si hay varios ".mp", elimina los extra y deja ".mp3".

        # Si no termina con ".mp3", se lo agregamos
        if not nuevo_nombre.endswith('.mp3'):
            nuevo_nombre += '.mp3'

        # Verificar si el nombre ya existe
        base_nombre, extension = os.path.splitext(nuevo_nombre)
        contador = 1
        while nuevo_nombre in nombres_existentes:
            nuevo_nombre = f'{base_nombre} duplicado-{contador}{extension}'
            contador += 1

        nombres_existentes[nuevo_nombre] = 1

        # Renombrar el archivo si el nombre cambió (o si es el mismo, pero en minúsculas)
        ruta_antigua = os.path.join(ruta_carpeta, nombre_archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
        if ruta_antigua != ruta_nueva:
            os.rename(ruta_antigua, ruta_nueva)
            print(f'Renombrado: {nombre_archivo} -> {nuevo_nombre}')