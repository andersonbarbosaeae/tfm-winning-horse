import streamlit as st
from utils import contentPage as cp
from utils import data as data

df = data.get_data("data-predictions")
cp.simple_page(
    "Data Predicción",
    "📊",
    df,
    "Datos de las carreras que se utilizarán para la predicción",
)
