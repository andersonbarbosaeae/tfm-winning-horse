import streamlit as st
from utils import contentPage as cp
from utils import data as data

df = data.get_data("racecourses")
cp.simple_page(
    "Hipódromos",
    "🏟",
    df,
    "ABC"
)
