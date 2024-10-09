import os

# Directorio
ruta_carpeta = "D:\\DirectorioMusica"

# Recorremos los archivos en la carpeta
for nombre_archivo in os.listdir(ruta_carpeta):
    # Renombrar solo si es un archivo (no una carpeta)
    if os.path.isfile(os.path.join(ruta_carpeta, nombre_archivo)):
        
        nuevo_nombre = nombre_archivo.lower()

        # Verificar si el nombre cambió
        ruta_antigua = os.path.join(ruta_carpeta, nombre_archivo)
        ruta_nueva_temp = os.path.join(ruta_carpeta, "temp_" + nuevo_nombre)  # Nombre temporal
        ruta_nueva_final = os.path.join(ruta_carpeta, nuevo_nombre)

        # Renombrar temporalmente (para que funcione en Windows)
        if ruta_antigua != ruta_nueva_temp:
            os.rename(ruta_antigua, ruta_nueva_temp)

        # Renombrar al nombre final en minúsculas
        if ruta_nueva_temp != ruta_nueva_final:
            os.rename(ruta_nueva_temp, ruta_nueva_final)
        
        print(f'Renombrado: {nombre_archivo} -> {nuevo_nombre}')