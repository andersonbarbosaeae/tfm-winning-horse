import streamlit as st
from utils import contentPage as cp
from utils import data as data

df = data.get_data("owners")
cp.simple_page(
    "Propietarios",
    "🕴🏼",
    df,
    "ABC"
)
