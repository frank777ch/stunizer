import tkinter as tk
from utils import *
from modulos import *
from interfaz import *

root = tk.Tk()
root.title("Stunizer")
root.iconbitmap("./assets/stunizer.ico")
root.geometry("500x400")
root.resizable(False, False)

mostrar_bienvenida(root)

boton1 = BotonGeneral(root, "Organizar carpetas por curso", funcion=organizar_por_curso)
boton2 = BotonGeneral(root, "Organizar carpetas por ciclo", funcion=organizar_por_ciclo)
boton3 = BotonGeneral(root, "Organizar carpetas por plan de estudios", funcion=organizar_por_plan)
boton4 = BotonGeneral(root, "Salir del programa", funcion=root.destroy)

boton1.pack(pady=5)
boton2.pack(pady=5)
boton3.pack(pady=5)
boton4.pack(pady=5)

root.mainloop()