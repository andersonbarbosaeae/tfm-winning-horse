import streamlit as st
from utils import data as data

# Config
st.set_page_config(page_title="Predicción", page_icon="🏅", layout="wide")

# Title
st.title("🏅 Predicción")
st.write(
    """
    En esta sección podrás introducir los datos de una carrera y predecir el resultado de la misma. Selecciona las variables que quieres utilizar para la predicción.
    """
)

# Data Sources
dfForm = data.get_data("form-predictions")
dataFormResults = {}

# Form
with st.form("template_form"):
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)
    col13, col14, col15, col16 = st.columns(4)
    col17, col18, col19, col20 = st.columns(4)

    # HorseName
    with col1:
        dataFormResults["HorseName"] = st.selectbox("HorseName", dfForm["HorseName"])
    # Region
    with col2:
        dataFormResults["Region"] = st.selectbox("Region", dfForm["Region"])
    # Distance
    with col3:
        dataFormResults["Distance"] = st.selectbox("Distance", dfForm["Distance"])
    # Category
    with col4:
        dataFormResults["Category"] = st.selectbox("Category", dfForm["Category"])
    # MajorEvent
    with col5:
        dataFormResults["MajorEvent"] = st.selectbox("MajorEvent", dfForm["MajorEvent"])
    # GroundCondition
    with col6:
        dataFormResults["GroundCondition"] = st.selectbox(
            "GroundCondition", dfForm["GroundCondition"]
        )
    # Stick
    with col7:
        dataFormResults["Stick"] = st.selectbox("Stick", dfForm["Stick"])
    # StartingStall
    with col8:
        dataFormResults["StartingStall"] = st.selectbox(
            "StartingStall", dfForm["StartingStall"]
        )
    # Weight
    with col9:
        dataFormResults["Weight"] = st.selectbox("Weight", dfForm["Weight"])
    # JockeyName
    with col10:
        dataFormResults["JockeyName"] = st.selectbox("JockeyName", dfForm["JockeyName"])
    # ChampionshipType
    with col11:
        dataFormResults["ChampionshipType"] = st.selectbox(
            "ChampionshipType", dfForm["ChampionshipType"]
        )
    # OwnerName
    with col12:
        dataFormResults["OwnerName"] = st.selectbox("OwnerName", dfForm["OwnerName"])
    # EdadYears
    with col13:
        dataFormResults["EdadYears"] = st.selectbox("EdadYears", dfForm["EdadYears"])
    # FAVORITE
    with col14:
        dataFormResults["FAVORITE"] = st.selectbox("FAVORITE", dfForm["FAVORITE"])
    # TrackHandedness
    with col15:
        dataFormResults["TrackHandedness"] = st.selectbox(
            "TrackHandedness", dfForm["TrackHandedness"]
        )
    # RaceCriteria_JUMP
    with col16:
        dataFormResults["RaceCriteria_JUMP"] = st.selectbox(
            "RaceCriteria_JUMP", dfForm["RaceCriteria_JUMP"]
        )
    # Seasons
    with col17:
        dataFormResults["Seasons"] = st.selectbox("Seasons", dfForm["Seasons"])
    # Schedule
    with col18:
        dataFormResults["Schedule"] = st.selectbox("Schedule", dfForm["Schedule"])

    # Submit button
    submit_button = st.form_submit_button(label="🔎 Predecir")

# Content
if submit_button:
    result = data.getPredictions(dataFormResults)
    # st.write(len(result.columns))
    # st.write(result)

    st.balloons()
    st.subheader("🏆 Resultado")
    c1, c2, c3 = st.columns(3)
    with c1:
        icon = "🏁" if result[0][2] == 1 else "❌"
        st.warning(f"**Primer Lugar:&nbsp;&nbsp;&nbsp; {icon}**", icon="🥇")
    with c2:
        icon = "🏁" if result[0][1] == 1 else "❌"
        st.success(f"**Primeros 3:&nbsp;&nbsp;&nbsp; {icon}**", icon="🥉")
    with c3:
        icon = "🏁" if result[0][0] == 1 else "❌"
        st.info(f"**Primeros 5:&nbsp;&nbsp;&nbsp; {icon}**", icon="🏅")
