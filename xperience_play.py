import streamlit as st
import pandas as pd
import gdown ## Descargar archivos de drive
import numpy as np
from cosine_similitud import similitud_coseno
from bayesian import calcular_top_items_bayesian
import requests

# Configurar la página para modo ancho
st.set_page_config(layout="wide")

# URL directa de la imagen en GitHub
# img_url = 'https://cdn.pixabay.com/photo/2013/08/26/09/40/silhouette-175970_1280.jpg'
# img_url = 'https://editor.analyticsvidhya.com/uploads/76889recommender-system-for-movie-recommendation.jpg'
img_url = 'https://static.wixstatic.com/media/8d7970_9a0ca002a61144d19b6ed5ea34107bab~mv2.png/v1/fill/w_980,h_551,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/8d7970_9a0ca002a61144d19b6ed5ea34107bab~mv2.png'

# Configura la imagen de fondo usando HTML y CSS
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("{img_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
'''
# Renderiza el código HTML y CSS en la aplicación
st.markdown(page_bg_img, unsafe_allow_html=True)


##########  TÍTULO DEL RECOMENDADOR DE PELÍCULAS  ##########

st.image('https://drive.google.com/file/d/1d6I0oklif-fKPglj2MNq9vsy1IQh07Yk/view?usp=drive_link', width=1000)
# st.title('    :film_projector: MOVIE RECOMMENDER :popcorn:')

# Centramos el título con Markdown y CSS
st.markdown("""
    <h1 style='text-align: center;'>
        🎬 XPERIENCE PLAY 🍿
    </h1>
    """, unsafe_allow_html=True)


##########  CARGAMOS LAS BASES DE DATOS  ##########

## Descargando base de datos df_final
url_final = 'https://drive.google.com/file/d/1O0XtSo0sd_qhtekPpK6HZNyja_YWXFui/view?usp=drive_link'
output_final = 'df_final.csv'
gdown.download(url_final, output_final, fuzzy=True, quiet=False)
df_final = pd.read_csv(output_final)

## Descargando base de datos df_vectorizer
url_vectorizer = 'https://drive.google.com/file/d/16GdMwYQrF26XZ4JWC0QnK6ICQdVbdDRY/view?usp=drive_link'
output_vectorizer = 'df_vectorizer.csv'
gdown.download(url_vectorizer, output_vectorizer, fuzzy=True, quiet=False)
df_vectorizer = pd.read_csv(output_vectorizer)

## Descargando la matriz similitud de coseno .npy
url_cosine = 'https://drive.google.com/file/d/1tdplDRklLoWigx4V5bDfbU-ZO0r8nZ72/view?usp=drive_link'
output_cosine = 'array.npy'
gdown.download(url_cosine, output_cosine, fuzzy=True, quiet=False)
data = np.load(output_cosine)
cosine = data['arr']


##########  CREAMOS EL SELECTBOX PARA SELECCIONAR PELÍCULAS  ##########

df = df_final.groupby('title')['title'].first()
option = st.selectbox(
    "CHOOSE A MOVIE:", df.tolist())


##########  MOSTRAMOS DATOS DE LA PELÍCULA SELECCIONADA  ##########

if option:
    # Filtrar el DataFrame según la opción seleccionada
    df_title_tmdbId = df_final.groupby('title')['tmdbId'].first().reset_index()
    api_key = '53881244403c42cb58048b62e1d8fa71'
    tmdb_id = df_title_tmdbId[df_title_tmdbId['title'] == f"{option}"]['tmdbId'].tolist()[0]
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    # Creamos 2 columnas: una para la imagen, otra para la descripción
    col1, col2 = st.columns([1, 3], vertical_alignment="center")  # [1, 2] indica que la segunda columna será el doble de ancha que la primera

    # Colocamos el póster en la primera columna
    with col1:
        poster_url = 'https://image.tmdb.org/t/p/w500' + movie_data['poster_path']
        st.image(poster_url, width=200)

    # Colocamos la información en la segunda columna
    with col2:
        st.link_button(f"**TITLE:** {df_final[df_final['tmdbId'] == tmdb_id]['title'].tolist()[0]}", 
                       f"https://www.themoviedb.org/movie/{tmdb_id}", use_container_width=True)
        st.write(f"**GENRES:** {df_final[df_final['tmdbId'] == tmdb_id]['genres'].tolist()[0]}")
        st.write(f"**OVERVIEW:** {movie_data['overview']}")
        st.write(f"**RELEASE DATE:** {movie_data['release_date']}")
        st.write(f"**DURATION:** {movie_data['runtime']} min")
        st.write(f"**RANKING:** ⭐({movie_data['popularity']})")

else:
    st.write('*** Selecciona una película ***')

# Línea de separación
st.markdown("---")

            ##########  MÉTODO BAYESIANO  ##########
##########  DETERMINAMOS LAS PELÍCULAS MÁS POPULARES  ##########

top_10_bayesian_recomendaciones = calcular_top_items_bayesian(df_final)
st.subheader('**MOST POPULAR MOVIES:** ')

## Consiguiendo los posters de las películas más populares
poster_populares = []
tmdbId_bayesian = []
for i, valor in enumerate(top_10_bayesian_recomendaciones['tmdbId'].tolist()):
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_1 = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    poster_url_1 = 'https://image.tmdb.org/t/p/w500' + movie_data_1['poster_path']
    poster_populares.append(poster_url_1)
    tmdbId_bayesian.append(valor)


# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas
cols_bayesian = st.columns(len(poster_populares))

# Iteramos sobre cada película y su respectiva columna
for i, (tmdb_id,url) in enumerate(zip(tmdbId_bayesian, poster_populares)):


    with cols_bayesian[i]:

        # URL del endpoint de videos
        video_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}/videos?api_key={api_key}&language=en-US"

        # Realizar la solicitud GET
        response = requests.get(video_url)
        data = response.json()

        # Obtener el primer tráiler (si está disponible)
        if 'results' in data and len(data['results']) > 0:
            trailer = next((video for video in data['results'] if video['type'] == 'Trailer'), None)
            if trailer:
                trailer_url = f"https://www.youtube.com/watch?v={trailer['key']}"

        st.link_button("Trailer", trailer_url, use_container_width=True)
        st.image(url, width=img_width)
        st.link_button("See more", f"https://www.themoviedb.org/movie/{tmdb_id}", use_container_width=True)
        # st.page_link(trailer_url, label="Trailer", icon="📺")
        

# Línea de separación
st.markdown("---")
                       
          ##########  SIMILITUD DE COSENO  ##########
##########  DETERMINAMOS LAS PELÍCULAS RECOMENDADAS  ##########

## Mostrando la similitud de coseno de la película especifica
df_similitud_coseno = similitud_coseno(option, df_vectorizer, cosine)
st.subheader('**WHY YOU LIKED:** ' + option)

## Consiguiendo los títulos y posters de las películas recomendadas
poster_recomendadas = []
tmdbId_coseno = []
for i, valor in enumerate(df_similitud_coseno['tmdbId'].tolist()):
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_2 = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    poster_url_2 = 'https://image.tmdb.org/t/p/w500' + movie_data_2['poster_path']
    poster_recomendadas.append(poster_url_2)
    tmdbId_coseno.append(valor)

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas
cols_cosine = st.columns(len(poster_recomendadas))

# Iteramos sobre cada película y su respectiva columna
for i, (tmdb_id, url) in enumerate(zip(tmdbId_coseno, poster_recomendadas)):

    # URL del endpoint de videos
    video_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}/videos?api_key={api_key}&language=en-US"

    # Realizar la solicitud GET
    response = requests.get(video_url)
    data = response.json()

    # Obtener el primer tráiler (si está disponible)
    if 'results' in data and len(data['results']) > 0:
        trailer = next((video for video in data['results'] if video['type'] == 'Trailer'), None)
        if trailer:
            trailer_url = f"https://www.youtube.com/watch?v={trailer['key']}"

    with cols_cosine[i]:
        st.link_button("Trailer", trailer_url, use_container_width=True)
        st.image(url, width=img_width)
        st.link_button("See more", f"https://www.themoviedb.org/movie/{tmdb_id}", use_container_width=True)

        # if st.button('Ver más', key=f'ver_mas_{i+10}', use_container_width=True):
        #     st.write(f'Detalles de {url}')
