import streamlit as st
import pandas as pd

# Config
st.set_page_config(page_title='Winning Horses', page_icon=':bar_chart:', layout='wide')

# Title
st.title('🏇 Winning Horses')

# Content
st.subheader('🔥 Motivación')
st.write(
    """
    Consideramos el mundo de la hípica y las carreras de caballos como un sector atractivo y creemos que permite una aplicación amplia e interesante del big data y la analítica de datos.
    """
)
st.subheader('🔎 Objetivo')
st.write(
    """
    Dentro de este ámbito, nuestra meta principal era crear un sistema que permitiese prever los resultados de las carreras de caballos antes de su celebración con cierto éxito. Finalmente, para este trabajo, lo hemos enfocado en definir las probabilidades de ganar de cada caballo, así como de su clasificación entre los 3 o 5 primeros.
    También hemos propuesto los siguientes objetivos específicos, que esperamos estudiar más adelante:
    - Predecir, de la forma más ajustada posible, los resultados de las carreras de caballos y, con ello, reforzar las posibles elecciones en apuestas. De esta manera se permitiría a las casas de apuestas establecer correctamente las cuotas y, a los apostantes, se les daría información relevante para el juego.
    - Identificar los factores más determinantes a la hora de conseguir la victoria en una carrera.
    - Proporcionar información relevante a los dueños de caballos, que les permita elegir el entrenador o jockey más apropiado, así como las carreras que mejor se adecuen a las características del animal.
    - Establecer el valor real de cada caballo, basándose en sus resultados y características, con el fin de facilitar la compraventa de estos.
    - Determinar el periodo de actividad óptimo de los caballos de carreras
    - Conocer los eventos y/o hipódromos más exigentes para el caballo e identificar la propensión a la lesión de cada animal.
    """
)