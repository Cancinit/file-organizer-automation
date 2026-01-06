import os
import shutil

def ejecutar_organizador(ruta_elegida):

    extensiones = {
    ".pdf": "pdf's GG",
    ".docx": "words GG",
    ".doc": "words GG",
    ".jpg": "imagenes GG",
    ".png": "imagenes GG",
    ".txt": "blocs GG",
    ".zip": "comprimidos GG",
    ".rar": "comprimidos GG",
    ".exe": "programas GG",
    ".pptx": "power's GG",
    ".wav": "audios GG",
    ".xlsx": "excels GG",
    ".jpeg": "imagenes GG",
    ".mp3": "audios GG"
    }

    
    for archivo in os.listdir(ruta_elegida):
        nombre, extension = os.path.splitext(archivo)
        
        if extension.lower () in extensiones:
            carpeta_destino=os.path.join(ruta_elegida, extensiones[extension.lower()])
            
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            ruta_actual = os.path.join (ruta_elegida, archivo)
            ruta_nueva = os.path.join (carpeta_destino, archivo)

            shutil.move(ruta_actual, ruta_nueva)
            print(f"movido: {archivo} -> {extensiones[extension.lower()]}")

