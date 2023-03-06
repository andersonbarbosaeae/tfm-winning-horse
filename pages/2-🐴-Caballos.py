import pandas as pd
import streamlit as st
from utils import data as data

from streamlit_pandas_profiling import st_profile_report

# Config
st.set_page_config(page_title='Caballos', page_icon='🐴', layout='wide')

# Data Sources
dfHorses = data.get_data("horses")
pr = dfHorses.profile_report()

# Title
st.title('🐴 Caballos')
st.write(
    """
    Datos básicos de todos los caballos registrados, tanto los que compiten como los que no
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info(f"**Total Registros: {len(dfHorses):,}**", icon="📝")

# Content
tabTabla, tabInformacion, tabData = st.tabs(["Tabla", "Información Columnas", "Data Report"])

# Print table with the dfHorses dataframe
with tabTabla:
    st.dataframe(dfHorses)

# Print table with information about the columns of the dfHorses dataframe
with tabInformacion:
    dfInformacion = pd.DataFrame({
        "Tipo": dfHorses.dtypes,
        "Valores Nulos": dfHorses.isnull().sum(),
    })
    st.table(dfInformacion)

# Print report of
with tabData:
    st_profile_report(pr)






