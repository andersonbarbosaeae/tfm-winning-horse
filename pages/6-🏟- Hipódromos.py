import folium
import streamlit as st
from streamlit_folium import st_folium

from utils import contentPage as cp
from utils import data as data

# Data Sources
df = data.get_data("racecourses")

# Page
tabTabla, tabInformacion, tabData, tabDataVisualizations = cp.simple_page(
    "Hipódromos",
    "🏟",
    df,
    "ABC"
)

# Data Visualization
with tabDataVisualizations:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Mapa de los hipódromos")
        showMap = st.checkbox('Ver mapa de los hipódromos')
        if showMap:
            m = folium.Map(
                location=[df.LATITUDE.mean(), df.LONGITUDE.mean()],
                zoom_start=5,
                tiles="OpenStreetMap",
            )
            for index, row in df.iterrows():
                name = f"{row.NAME}, {row.TYPE}"
                folium.Marker(
                    location=[row["LATITUDE"], row["LONGITUDE"]],
                    popup=name,
                    tooltip=name,
                ).add_to(m)
            st_folium(m, width=700, height=400)

