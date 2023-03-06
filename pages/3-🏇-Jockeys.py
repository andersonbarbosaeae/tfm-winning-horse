import streamlit as st
from utils import contentPage as cp
from utils import data as data

df = data.get_data("jockeys")
cp.simple_page(
    "Jockeys",
    "🏇",
    df,
    "Datos básicos de todos los jockeys registrados en las carreras de caballos"
)
