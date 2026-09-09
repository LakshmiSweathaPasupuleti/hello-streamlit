import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.header("Guessing game")

st.write("These are most engaging movies ever made! I like all of them but can you guess my ultimate favorite of them?")

movies = ["Interstellar", "The Dark Knight", "Forest Gump", "KillBill", "A Beautiful Mind"]

guess = st.selectbox("Guess my favorite one:", movies)

if st.button("Submit"):
    if guess == "The Dark Knight":
        st.success("Hurray! The Dark Knight is my favorite movie!")
        st.balloons()
    else:
        st.error("Oops wrong guess! Try again")