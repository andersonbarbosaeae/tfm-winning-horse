# Libraries
import streamlit as st
import pandas as pd

# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    if query == "horses":
        return pd.read_csv("data/horses.csv")
    if query == "results-global":
        pd2020 = pd.read_csv("data/Results_Global_2020_winnersTop_nuevo.csv")
        pd2021 = pd.read_csv("data/Results_Global_2021_winnersTop_nuevo.csv")
        pd2022 = pd.read_csv("data/Results_Global_2022_winnersTop_nuevo.csv")
        return pd.concat([pd2020, pd2021, pd2022])
    return None