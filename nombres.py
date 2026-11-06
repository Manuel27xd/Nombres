import random
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Medidor de Fidelidad", page_icon="💘", layout="centered"
)

st.title("💔 Medidor de Fidelidad 💘")
st.write("Escribe un nombre para descubrir la verdad:")

# Campo de texto en Streamlit
nombre = st.text_input("Nombre de la persona:")

# Botón para calcular
if st.button("Calcular Fidelidad"):
  if not nombre.strip():
    st.warning("⚠️ Por favor, escribe un nombre antes de calcular.")
  else:
    # Usamos la suma de los códigos ASCII como semilla
    # para que el mismo nombre siempre dé el mismo resultado.
    semilla = sum(ord(c) for c in nombre.lower().strip())
    random.seed(semilla)

    porcentaje = random.randint(0, 100)

    # Mostramos los resultados usando alertas nativas de Streamlit
    if porcentaje >= 80:
      st.success(
          f"¡100% Fiel! 💍❤️\n\n**{nombre.strip()}** es una persona sumamente"
          " leal."
      )
    elif porcentaje >= 50:
      st.warning(
          f"Dudoso (**{porcentaje}%** de fidelidad). 🤔\n\nMira bien las"
          " señales..."
      )
    else:
      st.error(
          f"¡Peligro total! 🚩\n\n**{nombre.strip()}** tiene alma de bandido/a."
      )