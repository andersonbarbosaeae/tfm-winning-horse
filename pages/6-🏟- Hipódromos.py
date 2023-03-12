import folium
import streamlit as st
from streamlit_folium import st_folium

from utils import contentPage as cp
from utils import data as data

# Data Sources
df = data.get_data("racecourses")

# Data Visualization
def dataVisualization():
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

# Page
cp.simple_page(
    "Hipódromos",
    "🏟",
    df,
    "ABC",
    dataVisualization
)
