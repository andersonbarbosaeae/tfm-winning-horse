# Libraries
import streamlit as st
import pandas as pd

# Config
pathVisualizations = "data/visualizations/"

# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    if query == "horses":
        df = pd.read_csv(pathVisualizations + "horses.csv")
        df.SEX = df.SEX.fillna("UNREGISTERED")
        return df
    if query == "jockeys":
        return pd.read_csv(pathVisualizations + "jockeys.csv")
    if query == "owners":
        return pd.read_csv(pathVisualizations + "owners.csv")
    if query == "racecourses":
        return pd.read_csv(pathVisualizations + "racecourses.csv")
    if query == "races":
        return pd.read_csv(pathVisualizations + "races.csv")
    if query == "trainers":
        return pd.read_csv(pathVisualizations + "trainers.csv")
    return None