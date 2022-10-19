import streamlit as st
import pandas as pd
import joblib
import requests

from tmdbv3api import Movie, TMDb
tmdb = TMDb()
tmdb.api_key = 'API here'
tmdb_movie = Movie()

def fetch_poster(movie_id):
    if movie_id != None:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=API HERE&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path = "https://guardian.ng/wp-content/uploads/2019/09/Nollywood-Rockcity-FM-e1569221315847.jpg"
    return full_path

def recommend(title):
    index = movies.loc[movies["Title"] == title].index[0]
    similiar_movies = list(enumerate(similarity[index]))
    similiar_movies_index = sorted(similiar_movies, key=lambda x:x[1], reverse=True)
    movies_index = similiar_movies_index[1:10]


    movie = []
    poster = []
    for i in range(len(movies_index)):
        movie_name = movies_index[i][0]
        name = movies["Title"][movie_name]
        try:
            result = tmdb_movie.search(name)
            movie_id = result[0].id
        except:
            movie_id = None
        movie.append(movies["Title"][movie_name])
        poster.append(fetch_poster(movie_id))
    return movie, poster

similarity = joblib.load("similarity_joblib")
movies = pd.read_csv("movies.csv")

st.title("Naija Movie Recommender System")
st.text("Recommmending you movies based on what you want")
options = st.selectbox(
    "Type or select a movie from the dropdown",
    movies["Title"].values
)

if st.button('Show Recommendation'):
    st.text("NOTICE: Some of the images may not relate with the movie title")
    recommended_movie_names,recommended_movie_posters = recommend(options)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

    col7, col8, col9 = st.columns(3)
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])  
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])





