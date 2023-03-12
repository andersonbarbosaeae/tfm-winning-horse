import pandas as pd
import streamlit as st

from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def simple_page(title, icon, df, description, dataVisualization=None):
    # Config
    st.set_page_config(page_title=title, page_icon=icon, layout='wide')

    # Data Sources
    pr = df.profile_report()

    # Title
    st.title(f"{icon} {title}")
    st.write(description)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"**Total Registros: {len(df):,}**", icon="📝")

    # Content
    tabTabla, tabInformacion, tabData, tabDataVisualizations = st.tabs(["🚀 Tabla", "👀 Información Columnas", "📈 Data Report", "📊 Data Visualizations"])

    # Print table with the dfHorses dataframe
    with tabTabla:
        st.dataframe(df)

    # Print table with information about the columns of the dfHorses dataframe
    with tabInformacion:
        dfInformacion = pd.DataFrame({
            "Tipo": df.dtypes,
            "Valores Nulos": df.isnull().sum(),
        })
        st.table(dfInformacion)

    # Print report of
    with tabData:
        reportShow = st.checkbox('Ver reporte de datos, esta información puede tardar en cargar')
        if reportShow:
            st_profile_report(pr)

    with tabDataVisualizations:
        if dataVisualization:
            dataVisualization()
        else:
            st.warning('No hay ninguna visualización de datos disponible para esta página')
