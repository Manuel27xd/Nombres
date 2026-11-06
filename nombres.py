import random
import tkinter as tk
from tkinter import messagebox


def calcular_fidelidad():
  nombre = entry_nombre.get().strip()

  if not nombre:
    messagebox.showwarning("Advertencia", "Por favor, escribe un nombre.")
    return

  # Usamos la suma de los códigos ASCII de las letras como semilla
  # para que el mismo nombre siempre dé el mismo resultado.
  semilla = sum(ord(c) for c in nombre.lower())
  random.seed(semilla)

  porcentaje = random.randint(0, 100)

  # Determinamos el mensaje y el color según el porcentaje
  if porcentaje >= 80:
    veredicto = f"¡100% Fiel! 💍❤️\n{nombre} es una persona sumamente leal."
    color = "#2e7d32"  # Verde oscuro
  elif porcentaje >= 50:
    veredicto = f"Dudoso ({porcentaje}% de fidelidad). 🤔\nMira bien las señales..."
    color = "#f57c00"  # Naranja
  else:
    veredicto = f"¡Peligro total! 🚩\n{nombre} tiene alma de bandido/a."
    color = "#c62828"  # Rojo oscuro

  label_resultado.config(text=veredicto, fg=color)


# --- Configuración de la interfaz gráfica ---
root = tk.Tk()
root.title("Medidor de Fidelidad 💘")
root.geometry("400x380")
root.config(bg="#fce4ec")  # Color de fondo rosa claro

# Título
titulo = tk.Label(
    root,
    text="💔 Medidor de Fidelidad 💘",
    font=("Arial", 16, "bold"),
    bg="#fce4ec",
    fg="#ad1457",
)
titulo.pack(pady=20)

# Instrucción
label_instruccion = tk.Label(
    root,
    text="Escribe un nombre para descubrir la verdad:",
    font=("Arial", 11),
    bg="#fce4ec",
    fg="#333333",
)
label_instruccion.pack(pady=5)

# Campo de texto (Input)
entry_nombre = tk.Entry(root, font=("Arial", 14), justify="center")
entry_nombre.pack(pady=10, ipady=4, ipadx=10)

# Botón de calcular
btn_calcular = tk.Button(
    root,
    text="Calcular Fidelidad",
    font=("Arial", 12, "bold"),
    bg="#d81b60",
    fg="white",
    activebackground="#ad1457",
    activeforeground="white",
    command=calcular_fidelidad,
)
btn_calcular.pack(pady=15, ipadx=10, ipady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(
    root, text="", font=("Arial", 12, "bold"), bg="#fce4ec", justify="center"
)
label_resultado.pack(pady=15)

# Iniciar la aplicación
root.mainloop()