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
st.header("🌈🍜 Ex:2: MOVIE TRIVIA 🍰🌮")

my_data = pd.DataFrame({ 
    "Movies": ["Interstellar", "The Dark Knight", "Forest Gump", "KillBill", "A Beautiful Mind"],
    "ProductionCostsInMillions": [170, 180, 60, 30, 60 ],
    "HighestGrosser_Answer": [False, True, False, False, False]
})
st.write("Test your knowledge of world cuisines and delicious desserts!")

col1, col2 = st.columns(2)

#Question1:

with col1:
    st.subheader("🌎 Movie Challenge")
    st.write("Choose a movie and guess it's production budget")
    Movie = st.selectbox("Choose a movie:", my_data["Movies"],key= "Movies", index=None)
    budget = st.select_slider("💰 What was the production budget? (in $ millions)",
    options=np.arange(20, 201, 5),
    key="budget")
with col2:
    st.subheader("🤯 The collections fact")
    st.write("Which movie has collected more than a billion dollars worldwide?")
    Movie_highestgrosser = st.selectbox("Choose a Movie:", my_data["Movies"], key="Movie_grosser", index=None)

#Sumission:

if st.button("Submit", key="ex2"):
    correct_budget = my_data.loc[my_data["Movies"]== Movie, "ProductionCostsInMillions"].iloc[0]
    correct_grosser = my_data.loc[my_data["HighestGrosser_Answer"]==True, "Movies"].iloc[0]
    #if year == correct_year:
        #st.success("Hurray! Your guess is pretty correct!")
    ##else:
      #  st.error("😅 Missed in a bit!")
    #if dessert == correct_dessert:
     #   st.success("Yay right, Tiramisu is surprisingly young..! 🍰🍰🍰")
    #else:
    #    st.error("😅 Almost!")

    if budget == correct_budget and Movie_highestgrosser == correct_grosser:
        st.success("🎉🎉 PERFECT! You got both right! 👏")
        st.balloons()

        st.markdown("""
        <div style="font-size:50px; text-align:center;">
            👏 👏 👏 👏 👏
        </div>
        """, unsafe_allow_html=True)

    elif budget == correct_budget:
        st.success("Question 1 — Correct!👏👏👏")
        st.error("Question 2 —  Missed in a bit!😅")

    elif Movie_highestgrosser == correct_grosser:
        st.error("🌎 Question 1 — Not quite!")
        st.success("🤯 Question 2 — 🎉 Correct! The Dark Knight crossed $1 billion!")

    else:
        st.error("😅 Both answers are not quite right!")