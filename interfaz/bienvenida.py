import tkinter as tk

def mostrar_bienvenida(root):

    # Título
    titulo_label = tk.Label(
        root,
        text="¡Bienvenido a Stunizer! :-D",
        font=("Arial", 16, "bold"),
        fg="#333"
    )
    titulo_label.pack(pady=(10, 5))  # Menor espacio entre el título y la descripción

    # Crear un Frame para agregar márgenes
    frame_texto = tk.Frame(root, padx=20, pady=0)  # Márgenes laterales
    frame_texto.pack(fill="x", expand=False)

    # Texto con justificación
    texto_descripcion = tk.Text(
        frame_texto,
        wrap="word",  # Ajustar palabras para no cortar líneas
        font=("Arial", 12),
        fg="#555",
        bg=root["bg"],  # Fondo igual que el de la ventana principal
        bd=0,  # Sin bordes
        relief="flat",  # Sin relieve
        height=4,  # Altura aproximada del texto
    )
    texto_descripcion.insert(
        "1.0",
        "Stunizer te ayuda a organizar tus carpetas académicas de forma sencilla. Selecciona una de las opciones a continuación para comenzar."
    )
    texto_descripcion.config(state="disabled")  # Desactiva la edición del texto
    texto_descripcion.pack(fill="x", expand=False)