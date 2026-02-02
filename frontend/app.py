import streamlit as st
import pickle as pkl
import pandas as pd

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pkl.load(open('movie_dict.pkl', 'rb'))
similarity = pkl.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")

option = st.selectbox(
    "How would you like to be contacted?",
   movies['title'].values
)

st.write("You selected:", option)

if st.button("Recommend"):
    recommended = recommend(option)
    for i in recommended:
        st.write(i)