import tkinter as tk
from tkinter import filedialog
import organizador
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def seleccionar_direccion():
    ruta = filedialog.askdirectory()
    if ruta:
        label_status.configure(text=f"Seleccionado: ...{ruta[-25:]}", text_color="#AAAAAA")
        organizador.ejecutar_organizador(ruta) 
        label_status.configure(text="¡Organización completada! ✨", text_color="#00FF7F")

GRIS_FONDO = "#121212"
GRIS_TARJETA = "#1E1E1E"
GRIS_BOTON = "#333333"

root = ctk.CTk ()

root.title("organizador GG")
root.geometry("450x300")
root.configure(fg_color=GRIS_FONDO)

#texto de arriba
label=ctk.CTkLabel(root, 
text="bienvenido/a al acomodador de archivos! :D",
font=("Segoe UI", 18, "bold"),
text_color="#FFFFFF"
)
label.pack(pady=(30,10))

#subtitulo
texto_instrucciones = ("Selecciona una carpeta para ordenar\nsus archivos "
                      "automáticamente por tipo.")
label_sub = ctk.CTkLabel(
    root, 
    text=texto_instrucciones,
    text_color="#FFFFFF",
    font=("Segoe UI", 16)
)
label_sub.pack(pady=10)

boton = ctk.CTkButton(root, #config del botoncito
text="Haga click aquí para iniciar :)", 
hover_color="#444444",
text_color="white",
corner_radius=10,
height=40, 
fg_color= GRIS_BOTON, 
command= seleccionar_direccion,
)
boton.pack(pady=20)

label_status = ctk.CTkLabel(root, text="", font=("Segoe UI", 12))
label_status.pack(pady=10)

root.mainloop()