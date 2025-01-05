import tkinter as tk

from .curso import organizar_por_curso
from .ciclo import organizar_por_ciclo
from .plan_estudios import organizar_por_plan

# Define qué funcionalidades estarán disponibles al importar el paquete 'modulos'
__all__ = ["organizar_por_curso", "organizar_por_ciclo", "organizar_por_plan"]