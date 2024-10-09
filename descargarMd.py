import requests
import os

# URL del archivo a descargar
url = "https://static.platzi.com/media/public/uploads/principios_de_usabilidad_a50ee480-9541-4c7e-90c6-419169c5e91e.md"

# Nombre con el que se guardará el archivo
file_name = url.split("/")[-1]

# Ruta donde se guardará el archivo
file_path = os.path.join(os.getcwd(), file_name)

# encabezados para simular una solicitud de navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# petición GET para descargar el archivo
response = requests.get(url, headers=headers)

# Guardar el archivo si la respuesta es exitosa (código 200)
if response.status_code == 200:
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Archivo descargado y guardado como: {file_path}")
else:
    print(f"Error al descargar el archivo. Código de estado: {response.status_code}")