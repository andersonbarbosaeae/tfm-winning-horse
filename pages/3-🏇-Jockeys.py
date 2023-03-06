import pandas as pd
import streamlit as st
from utils import data as data

from streamlit_pandas_profiling import st_profile_report

# Config
st.set_page_config(page_title='Jockeys', page_icon='🏇', layout='wide')

# Data Sources
dfJockeys = data.get_data("jockeys")
pr = dfJockeys.profile_report()

# Title
st.title('🏇 Jockeys')
st.write(
    """
    Datos básicos de todos los jockeys registrados en las carreras de caballos 
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info(f"**Total Registros: {len(dfJockeys):,}**", icon="📝")

# Content
tabTabla, tabInformacion, tabData = st.tabs(["Tabla", "Información Columnas", "Data Report"])

# Print table with the dfHorses dataframe
with tabTabla:
    st.dataframe(dfJockeys)

# Print table with information about the columns of the dfHorses dataframe
with tabInformacion:
    dfInformacion = pd.DataFrame({
        "Tipo": dfJockeys.dtypes,
        "Valores Nulos": dfJockeys.isnull().sum(),
    })
    st.table(dfInformacion)

# Print report of
with tabData:
    st_profile_report(pr)
