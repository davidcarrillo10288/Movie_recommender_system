import streamlit as st
import pandas as pd
import gdown ## Descargar archivos de drive
import numpy as np
from cosine_similitud2 import similitud_coseno
from bayesian import calcular_top_items_bayesian
import requests
import os

# Configurar la página para modo ancho
st.set_page_config(layout="wide")

# URL directa de la imagen en GitHub
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

# st.image('https://drive.google.com/file/d/1d6I0oklif-fKPglj2MNq9vsy1IQh07Yk/view?usp=drive_link', width=1000)
# st.title('    :film_projector: MOVIE RECOMMENDER :popcorn:')

# Centramos el título con Markdown y CSS
st.markdown("""
    <h1 style='text-align: center;'>
        🎬 XPERIENCE PLAY 🍿
    </h1>
    """, unsafe_allow_html=True)


##########  CARGAMOS LAS BASES DE DATOS  ##########

## Descargando base de datos df_final
# url_final = 'https://drive.google.com/file/d/1O0XtSo0sd_qhtekPpK6HZNyja_YWXFui/view?usp=drive_link'
output_final = 'df_final.csv'
# gdown.download(url_final, output_final, fuzzy=True, quiet=False)

# ID del archivo de Google Drive
file_id = '1O0XtSo0sd_qhtekPpK6HZNyja_YWXFui'
# URL de descarga directa de Google Drive
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
# Usa wget para descargar el archivo
os.system(f'wget --no-check-certificate -O {output_final} {download_url}')
df_final = pd.read_csv(output_final)

## Descargando base de datos df_vectorizer
# url_vectorizer = 'https://drive.google.com/file/d/16GdMwYQrF26XZ4JWC0QnK6ICQdVbdDRY/view?usp=drive_link'
output_vectorizer = 'df_vectorizer.csv'
# gdown.download(url_vectorizer, output_vectorizer, fuzzy=True, quiet=False)
# ID del archivo de Google Drive

file_id = '16GdMwYQrF26XZ4JWC0QnK6ICQdVbdDRY'
# URL de descarga directa de Google Drive
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
# Usa wget para descargar el archivo
os.system(f'wget --no-check-certificate -O {output_vectorizer} {download_url}')
df_vectorizer = pd.read_csv(output_vectorizer)

## Descargando la matriz similitud de coseno .npy
# url_cosine = 'https://drive.google.com/file/d/1tdplDRklLoWigx4V5bDfbU-ZO0r8nZ72/view?usp=drive_link'
output_cosine = 'array.npy'
# gdown.download(url_cosine, output_cosine, fuzzy=True, quiet=False)
# ID del archivo de Google Drive

file_id = '1tdplDRklLoWigx4V5bDfbU-ZO0r8nZ72'
# URL de descarga directa de Google Drive
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
# Usa wget para descargar el archivo
os.system(f'wget --no-check-certificate -O {output_cosine} {download_url}')
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


    # if response.status_code == 200:
    #     movie_data = response.json()
    # else:
    #     print("Error en la solicitud:", response.status_code)
    
#     # Verificar si 'poster_path' está disponible
#     if movie_data.get('poster_path'):

#         # Creamos 2 columnas: una para la imagen, otra para la descripción
#         col1, col2 = st.columns([1, 3], vertical_alignment="center")  # [1, 2] indica que la segunda columna será el doble de ancha que la primera

#         # Colocamos el póster en la primera columna
#         with col1:
#             poster_url = 'https://image.tmdb.org/t/p/w500' + movie_data['poster_path']
#             st.image(poster_url, width=200)

#         # Colocamos la información en la segunda columna
#         with col2:
#             st.link_button(f"**TITLE:** {df_final[df_final['tmdbId'] == tmdb_id]['title'].tolist()[0]}", 
#                         f"https://www.themoviedb.org/movie/{tmdb_id}", use_container_width=True)
#             st.write(f"**GENRES:** {df_final[df_final['tmdbId'] == tmdb_id]['genres'].tolist()[0]}")
#             st.write(f"**OVERVIEW:** {movie_data['overview']}")
#             st.write(f"**RELEASE DATE:** {movie_data['release_date']}")
#             st.write(f"**DURATION:** {movie_data['runtime']} min")
#             st.write(f"**RANKING:** ⭐({movie_data['popularity']})")
#     else:
#         # Mostrar mensaje si no hay póster disponible
#         st.write("La información de la película no está disponible para mostrar. Por favor, seleccione otra película.")

# else:
#     st.write('*** Selecciona una película ***')


# Verificamos el estado de la respuesta
if response.status_code == 200:
    movie_data = response.json()

    # Verificamos si hay datos disponibles y si el póster está presente
    if movie_data:
        poster_path = movie_data.get('poster_path')
        if poster_path:
            # Creamos 2 columnas: una para la imagen, otra para la descripción
            col1, col2 = st.columns([1, 2], vertical_alignment="center")

            # Colocamos el póster en la primera columna
            with col1:
                poster_url = 'https://image.tmdb.org/t/p/w500' + poster_path
                st.image(poster_url, width=300)
                
                # sentiment_mapping = ["one", "two", "three", "four", "five"]
                # selected = st.feedback("stars")
                # if selected is not None:
                #     st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

            # Colocamos la información en la segunda columna
            with col2:
                st.link_button(f"**TITLE:** {movie_data.get('title', 'Título no disponible')}", 
                               f"https://www.themoviedb.org/movie/{tmdb_id}", use_container_width=True)
                st.write(f"**GENRES:** {', '.join(genre['name'] for genre in movie_data.get('genres', []))}")
                st.write(f"**OVERVIEW:** {movie_data.get('overview', 'Descripción no disponible')}")
                st.write(f"**RELEASE DATE:** {movie_data.get('release_date', 'Fecha de lanzamiento no disponible')}")
                st.write(f"**DURATION:** {movie_data.get('runtime', 'Duración no disponible')} min")
                st.write(f"**POPULARITY:** ⭐({movie_data.get('popularity', 'Popularidad no disponible')})")
                
                # Línea de separación
                st.markdown("---")

                # Colocar el slider y la representación de estrellas dentro de la columna col2
                col_rating, col_stars = st.columns([1,4])

                # Slider para seleccionar calificación de estrellas (1 a 5)
                with col_rating:
                    rating = st.slider("RANKING", min_value=1, max_value=5, value=1)

                # Mostrar las estrellas de acuerdo a la calificación seleccionada
                with col_stars:
                    st.write("⭐" * rating)
                
                # # Línea de separación
                # st.markdown("---")

        else:
            # Mostramos este mensaje si no hay póster disponible
            st.write("La información de la película no está disponible para mostrar. Por favor, seleccione otra película.")
    else:
        # Mostramos este mensaje si no se recibe información de la película
        st.write("La información de la película no está disponible. Por favor, seleccione otra película.")

else:
    # Mostramos este mensaje si la solicitud falla
    st.write("Error en la solicitud de la película. Por favor, intente con otra película.")

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
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_similitud_coseno['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_2 = response.json()
    else:
        print("Error en la solicitud:", response.status_code)

    if 'poster_path' in movie_data_2 and movie_data_2["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_2["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor
    # poster_url_2 = 'https://image.tmdb.org/t/p/w500' + movie_data_2['poster_path']
    # poster_recomendadas.append(poster_url_2)
    # tmdbId_coseno.append(valor)

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas
cols_cosine = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url, tmdb_id) in enumerate(poster_dict.items()):

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

# Línea de separación
st.markdown("---")

          ##########  POR TIPO DE PELÍCULA  ##########
##########  DETERMINAMOS LAS PELÍCULAS RECOMENDADAS  ##########

df_type = pd.DataFrame({
    'rating': df_final.groupby('title')['rating'].first(),
    'genres': df_final.groupby('title')['genres'].first(),
    'tmdbId': df_final.groupby('title')['tmdbId'].first(),
    'year': df_final.groupby('title')['year'].first()
}).reset_index()

###### DRAMA ######

df_drama = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Drama'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**DRAMA:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_drama['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_drama = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_drama[i]:

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


# Línea de separación
st.markdown("---")

###### ACTION ######

df_action = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Action'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**ACTION:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_action['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_action = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_action[i]:

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


# Línea de separación
st.markdown("---")

###### HORROR ######

df_horror = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Horror'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**HORROR:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_horror['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_horror = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_horror[i]:

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


# Línea de separación
st.markdown("---")


###### Thriller ######

df_thriller = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Thriller'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**THRILLER:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_thriller['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_thriller = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_thriller[i]:

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


# Línea de separación
st.markdown("---")


###### Documentary ######

df_documentary = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Documentary'])].sort_values(by='rating', ascending=False).head(20)
# st.dataframe(df_documentary)
st.subheader('**DOCUMENTARY:** ')

## Consiguiendo los posters de las películas más populares
# poster_type = []
# tmdbId_type = []
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_documentary['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor
                # poster_type.append(poster_url_type)
                # tmdbId_type.append(valor)

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_documentary = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_documentary[i]:

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


# Línea de separación
st.markdown("---")


###### Comedy ######

df_comedy = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Comedy'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**COMEDY:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_comedy['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_comedy = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_comedy[i]:

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


# Línea de separación
st.markdown("---")


###### Science Fiction ######

df_sf = df_type[df_type['genres'].apply(lambda x: x.split('|') == ['Sci-Fi'])].sort_values(by='rating', ascending=False).head(20)

st.subheader('**SCIENCE FICTION:** ')

## Consiguiendo los posters de las películas más populares
# Diccionario para mantener la relación entre poster URL y TMDB ID
poster_dict = {}
for i, valor in enumerate(df_sf['tmdbId'].tolist()):
    if len(poster_dict) >=10:
        break
    api_key = '53881244403c42cb58048b62e1d8fa71'
    url = f'https://api.themoviedb.org/3/movie/{valor}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data_type = response.json()
    else:
        print("Error en la solicitud:", response.status_code)
    
    if 'poster_path' in movie_data_type and movie_data_type["poster_path"]:
        poster_url_type = 'https://image.tmdb.org/t/p/w500' + movie_data_type["poster_path"]

        # Agregar el poster y el TMDB ID al diccionario si el poster URL no está ya en el diccionario
        if poster_url_type not in poster_dict:
                poster_dict[poster_url_type] = valor

# Centrar contenido y ajustar el tamaño
img_width = 140  # Tamaño uniforme para las imágenes

# Creamos una fila con varias columnas basadas en la cantidad de posters únicos
cols_sf = st.columns(len(poster_dict))

# Iteramos sobre cada película y su respectiva columna
for i, (url,tmdb_id) in enumerate(poster_dict.items()):

    with cols_sf[i]:

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


# Línea de separación
st.markdown("---")