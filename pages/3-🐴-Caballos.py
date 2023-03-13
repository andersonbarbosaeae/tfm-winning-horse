import streamlit as st

import altair as alt
import numpy as np
import pandas as pd

from utils import contentPage as cp
from utils import data as data


df = data.get_data("horses")

def dataVisualization():
    c1, c2 = st.columns(2)
    source = df.SEX.value_counts().reset_index()
    source.columns = ['Genero', 'Cantidad']

    with c1:
        st.subheader("Genero")
        st.text("En las carreras de caballos, el genero es importante")
        optionsSex = st.multiselect(
            "Selecciona el genero",
            source.Genero,
            source.Genero,
        )
    with c2:
        # print Pie chart of SEX column of dfHorses dataframe
        st.subheader("Gráfico de torta")
        source = source[source.Genero.isin(optionsSex)]
        c = alt.Chart(source).mark_arc(innerRadius=50).encode(
            color=alt.Color(field="Genero", type="nominal"),
            theta=alt.Theta(field="Cantidad", type="quantitative"),
        )
        st.altair_chart(c, use_container_width=True)


cp.simple_page(
    "Caballos",
    "🐴",
    df,
    "Datos básicos de todos los caballos registrados, tanto los que compiten como los que no",
    dataVisualization
)




