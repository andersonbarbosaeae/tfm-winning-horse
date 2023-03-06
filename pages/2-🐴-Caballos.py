import streamlit as st
from utils import contentPage as cp
from utils import data as data

df = data.get_data("horses")
cp.simple_page(
    "Caballos",
    "🐴",
    df,
    "Datos básicos de todos los caballos registrados, tanto los que compiten como los que no"
)




