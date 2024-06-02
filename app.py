import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a3389b25d8ce04a45c3e0a4cf8ac6073&&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for j in movies_list:
            movie_id = movies.iloc[j[0]].movie_id
            recommended_movies.append(movies.iloc[j[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters

    except IndexError:
        st.error("Movie not found. Please select another movie.")

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('Movie Recommender')

selected_movie_name = st.selectbox("Pick a Movie You Love, and We'll Recommend More!", movies['title'].values)

if st.button("Recommend"):
    st.markdown("### Here are some Movies you might like: ")
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

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


st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #334;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
        .footer-content {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }
        .footer-content p {
            margin: 0;
            padding-right: 20px;
        }
        .footer-content a {
            color: #1E90FF;
            text-decoration: none;
            font-weight: bold;
        }
        .footer-content a:hover {
            color: #FF6347;
        }
    </style>
    <footer class='footer'>
        <div class='footer-content'>
            <a href='mailto:vineetchoubey.imp1@gmail.com'>Contact Me!</a>
            <a href='https://www.linkedin.com/in/vineet-choubey-136998200/' target='_blank'>LinkedIn</a>
            <a href='https://github.com/vineetc17' target='_blank'>GitHub</a>
        </div>
    </footer>
    """, unsafe_allow_html=True)

