import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

movies=pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3f972dbc71bc69f995da082db4704163&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    top_movies= sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in top_movies:
        recommended_movies.append(movies['title'][i[0]])
        recommended_movies_posters.append(fetch_poster(movies['movie_id'][i[0]]))
    return recommended_movies,recommended_movies_posters


st.title("Movie Recommender System")

selected_movie=st.selectbox("Select a movie",movies['title'].values)

if st.button("Recommend"):
    names,posters=recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])