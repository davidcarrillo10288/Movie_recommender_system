import streamlit as st
import pandas as pd
import gdown ## Descargar archivos de drive
import numpy as np
from cosine_similitud import similitud_coseno
import requests


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
st.title('    :film_projector: MOVIE RECOMMENDER :popcorn:')


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
    "Escoge una película:", df.tolist())


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
    col1, col2 = st.columns([1, 2])  # [1, 2] indica que la segunda columna será el doble de ancha que la primera

    # Colocamos el póster en la primera columna
    with col1:
        poster_url = 'https://image.tmdb.org/t/p/w500' + movie_data['poster_path']
        st.image(poster_url, width=200)

    # Colocamos la información en la segunda columna
    with col2:
        st.write(f"**Overview:** {movie_data['overview']}")
        st.write(f"**Año de realización:** {movie_data['release_date']}")
        st.write(f"**Duración:** {movie_data['runtime']} min")

else:
    st.write('*** Selecciona una película ***')


##########  DETERMINAMOS LAS PELÍCULAS RECOMENDADAS  ##########

## Mostrando la similitud de coseno de la película especifica
df_similitud_coseno = similitud_coseno(option, df_vectorizer, cosine)
st.subheader('**Películas Recomendadas:** ')

## Consiguiendo los títulos y posters de las películas recomendadas
original_title = []
poster_recomendadas = []
for i, valor in enumerate(df_similitud_coseno['tmdbId'].tolist()):
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_2 = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    poster_url_2 = 'https://image.tmdb.org/t/p/w500' + movie_data_2['poster_path']
    original_title.append(movie_data_2['original_title'])
    poster_recomendadas.append(poster_url_2)



# Primera fila de 5 columnas
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

with col1:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[0]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[0], width=img_width)

with col2:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[1]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[1], width=img_width)

with col3:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[2]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[2], width=img_width)

with col4:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[3]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[3], width=img_width)

with col5:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[4]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[4], width=img_width)

# Segunda fila de 5 columnas
col6, col7, col8, col9, col10 = st.columns([1, 1, 1, 1, 1])

with col6:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[5]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[5], width=img_width)

with col7:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[6]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[6], width=img_width)

with col8:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[7]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[7], width=img_width)

with col9:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[8]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[8], width=img_width)

with col10:
    with st.container():
        st.markdown(f"<h4 style='text-align: center; font-size: 16px;'>{original_title[9]}</h4>", unsafe_allow_html=True)
        st.image(poster_recomendadas[9], width=img_width)

## Imprimiendo el dataframe df_similitud_coseno
st.dataframe(df_similitud_coseno, use_container_width=True)