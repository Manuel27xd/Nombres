import random
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Medidor de Fidelidad", page_icon="💘", layout="centered"
)

# --- ESTILOS CSS PERSONALIZADOS (Tema Oscuro Neón) ---
st.markdown(
    """
    <style>
    /* Fondo general oscuro y elegante */
    .stApp {
        background: linear-gradient(135deg, #0f172a 1e-15%, #1e1b4b 100%);
    }

    /* Título principal con brillo neón */
    h1 {
        color: #38bdf8;
        text-align: center;
        text-shadow: 0px 0px 15px rgba(56, 189, 248, 0.4);
    }

    /* Textos generales */
    p, label {
        color: #e2e8f0;
        font-size: 1.1rem !important;
    }

    /* Personalización del botón (Degradado azul/morado) */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        border: none;
        box-shadow: 0px 4px 15px rgba(168, 85, 247, 0.4);
        width: 100%;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        transform: scale(1.02);
        box-shadow: 0px 6px 20px rgba(168, 85, 247, 0.6);
    }

    /* Caja de texto oscura con bordes brillantes */
    .stTextInput>div>div>input {
        background-color: #1e293b;
        color: #f8fafc;
        border-radius: 8px;
        border: 2px solid #6366f1;
    }

    /* Métrica y tarjetas */
    div[data-testid="stMetricValue"] {
        color: #38bdf8 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- INTERFAZ DE LA APP ---
st.title("💔 Medidor de Fidelidad 💘")
st.write(
    "<p style='text-align: center;'>Escribe un nombre para descubrir el"
    " porcentaje exacto de lealtad:</p>",
    unsafe_allow_html=True,
)

# Campo de texto
nombre = st.text_input("Nombre de la persona:")

# Botón para calcular
if st.button("✨ Calcular Fidelidad ✨"):
    if not nombre.strip():
        st.warning("⚠️ Por favor, escribe un nombre antes de calcular.")
    else:
        # Usamos la suma de los códigos ASCII como semilla
        semilla = sum(ord(c) for c in nombre.lower().strip())
        random.seed(semilla)

        porcentaje = random.randint(0, 100)

        st.markdown("---")

        # Mostramos el porcentaje en grande
        st.metric(
            label=f"Nivel de Fidelidad para: {nombre.strip()}",
            value=f"{porcentaje}%",
        )

        # Barra de progreso visual
        st.progress(porcentaje)

        # Mensaje según el porcentaje obtenido
        if porcentaje >= 80:
            st.success(
                f"¡Resultado Alto! 💍❤️ **{nombre.strip()}** demuestra ser una"
                " persona sumamente leal."
            )
        elif porcentaje >= 50:
            st.warning(
                f"Resultado Moderado. 🤔 Hay dudas en el ambiente, ¡mira bien las"
                " señales!"
            )
        else:
            st.error(
                f"¡Alerta Roja! 🚩 **{nombre.strip()}** marca un nivel de fidelidad"
                " muy bajo."
            )