# Libraries
import streamlit as st
import pandas as pd
import joblib

# Config
pathResults = "tfm/data/results/"
pathVisualizations = "tfm/data/visualizations/"


# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    if query == "horses":
        df = pd.read_csv(pathVisualizations + "horses.csv")
        df.SEX: df.SEX.fillna("UNREGISTERED")
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
    if query == "data-predictions":
        return pd.read_csv(pathResults + "winning_horse_limpieza.csv")
    if query == "form-predictions":
        return getFormPredictions()
    return None


def getFormPredictions():
    df = get_data("data-predictions")
    result = {
        "HorseName": df.HorseName.unique(),
        "Region": df.Region.unique(),
        "Distance": df.Distance.unique(),
        "Category": df.Category.unique(),
        "MajorEvent": df.MajorEvent.unique(),
        "GroundCondition": df.GroundCondition.unique(),
        "Stick": df.Stick.unique(),
        "StartingStall": df.StartingStall.unique(),
        "Weight": df.Weight.unique(),
        "JockeyName": df.JockeyName.unique(),
        "ChampionshipType": df.ChampionshipType.unique(),
        "OwnerName": df.OwnerName.unique(),
        "EdadYears": df.EdadYears.unique(),
        "FAVORITE": df.FAVORITE.unique(),
        "TrackHandedness": ["Left-Handed", "Right-Handed"],
        "RaceCriteria_JUMP": df.RaceCriteria_JUMP.unique(),
        "Seasons": ["Spring", "Summer", "Winter"],
        "Schedule": ["Midday", "Night"],
        "TOP": ["TOP1", "TOP3", "TOP5"],
    }
    return result


def getPredictions(form):
    # Reorganizamos la información
    form["TrackHandedness_Left-Handed"] = (
        1 if form["TrackHandedness"] == "Left-Handed" else 0
    )
    form["TrackHandedness_Right-Handed"] = (
        1 if form["TrackHandedness"] == "Right-Handed" else 0
    )
    form["Seasons_Spring"] = 1 if form["Seasons"] == "Spring" else 0
    form["Seasons_Summer"] = 1 if form["Seasons"] == "Summer" else 0
    form["Seasons_Winter"] = 1 if form["Seasons"] == "Winter" else 0
    form["Schedule_Midday"] = 1 if form["Schedule"] == "Midday" else 0
    form["Schedule_Night"] = 1 if form["Schedule"] == "Night" else 0
    form["TOP1"] = 1 if form["TOP"] == "TOP1" else 0
    form["TOP3"] = 1 if form["TOP"] == "TOP3" else 0
    form["TOP5"] = 1 if form["TOP"] == "TOP5" else 0
    del form["TrackHandedness"]
    del form["Seasons"]
    del form["Schedule"]
    del form["TOP"]

    Gnb = joblib.load("../models/Gnb.pkl")

    return form

    # result = {
    #     "Region": df.Region.unique(),
    #     "Distance": df.Distance.unique(),
    #     "Category": df.Category.unique(),
    #     "MajorEvent": df.MajorEvent.unique(),
    #     "GroundCondition": df.GroundCondition.unique(),
    #     "Stick": df.Stick.unique(),
    #     "StartingStall": df.StartingStall.unique(),
    #     "Weight": df.Weight.unique(),
    #     "JockeyName": df.JockeyName.unique(),
    #     "ChampionshipType": df.ChampionshipType.unique(),
    #     "OwnerName": df.OwnerName.unique(),
    #     "EdadYears": df.EdadYears.unique(),
    #     "FAVORITE": df.FAVORITE.unique(),
    #     TrackHandednessLeftHanded: df["TrackHandedness_Left-Handed"].unique(),
    #     TrackHandednessRightHanded: df["TrackHandedness_Right-Handed"].unique(),
    #     "RaceCriteria_JUMP": df.RaceCriteria_JUMP.unique(),
    #     "Seasons_Spring": df.Seasons_Spring.unique(),
    #     "Seasons_Summer": df.Seasons_Summer.unique(),
    #     "Seasons_Winter": df.Seasons_Winter.unique(),
    #     "Schedule_Midday": df.Schedule_Midday.unique(),
    #     "Schedule_Night": df.Schedule_Night.unique(),
    # }

    # result = {
    #     "HorseName": df.HorseName.unique(),
    #     "Region": df.Region.unique(),
    #     "Distance": df.Distance.unique(),
    #     "Category": df.Category.unique(),
    #     "MajorEvent": df.MajorEvent.unique(),
    #     "GroundCondition": df.GroundCondition.unique(),
    #     "Stick": df.Stick.unique(),
    #     "StartingStall": df.StartingStall.unique(),
    #     "Weight": df.Weight.unique(),
    #     "JockeyName": df.JockeyName.unique(),
    #     "ChampionshipType": df.ChampionshipType.unique(),
    #     "OwnerName": df.OwnerName.unique(),
    #     "EdadYears": df.EdadYears.unique(),
    #     "FAVORITE": df.FAVORITE.unique(),
    #     TrackHandedness: ["Left", "Right"],
    #     "RaceCriteria_JUMP": df.RaceCriteria_JUMP.unique(),
    #     "Seasons_Spring": df.Seasons_Spring.unique(),
    #     "Seasons_Summer": df.Seasons_Summer.unique(),
    #     "Seasons_Winter": df.Seasons_Winter.unique(),
    #     "Schedule_Midday": df.Schedule_Midday.unique(),
    #     "Schedule_Night": df.Schedule_Night.unique(),
    # }
