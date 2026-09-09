import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.header("Ex:1: Guessing game")

st.write("These are most engaging movies ever made! I like all of them but can you guess my ultimate favorite of them?")

movies = ["Interstellar", "The Dark Knight", "Forest Gump", "KillBill", "A Beautiful Mind"]

guess = st.selectbox("Guess my favorite one:", movies, index=None)

if st.button("Submit", key= "ex1"):
    if guess == "The Dark Knight":
        st.success("Hurray! The Dark Knight is my favorite movie!")
        st.balloons()
    else:
        st.error("Oops wrong guess! Try again")

import numpy as np
import pandas as pd
st.header("🌈🍜 Ex:2: FOOD TRIVIA 🍰🌮")

my_data = pd.DataFrame({ 
    "Cuisine": ["Italian", "Indian", "Chinese", "Mexican", "Japanese"],
    "Year": [1960, 1980, 1970, 1960, 1950],
    "Dessert": ["Tiramisu", "Gulab Jamun", "Mooncake", "Churros", "Mochi"],
    "Dessert_Answer": [True, False, False, False, False]
})
st.write("Test your knowledge of world cuisines and delicious desserts!")

col1, col2 = st.columns(2)

#Question1:

with col1:
    st.subheader("🩷🌎 Cuisine Challenge")
    st.write("Choose a cuisine and guess around which year it became popular worldwide.")
    cuisine = st.selectbox("Choose a cuisine:", my_data["Cuisine"],key= "Cuisine", index=None)

    year = st.select_slider("Around which year?", options = np.arange(1900, 2021, 10), key = "year")
with col2:
    st.subheader("💜🤯 The Food Fact")
    st.write("Which dessert was invented most recently?")
    dessert = st.selectbox("Choose a dessert:", my_data["Dessert"], key="dessert", index=None)

#Sumission:

if st.button("Submit", key="ex2"):
    correct_year = my_data.loc[my_data["Cuisine"]== cuisine, "Year"].iloc[0]
    correct_dessert = my_data.loc[my_data["Dessert_Answer"]==True, "Dessert"].iloc[0]
    if year == correct_year:
        st.success("Hurray! Your guess is pretty correct!")
    else:
        st.error("😅 Missed in a bit!")
    if dessert == correct_dessert:
        st.success("Yay right, Tiramisu is surprisingly young..! 🍰🍰🍰")
    else:
        st.error("😅 Almost!")