# MOVIE RECOMMENDER SYSTEM

Una reconocida plataforma de Streaming, nos proporciona de toda su data sobre las películas en su sistema, con la finalidad de poder crearle un recomendador de películas virtual. De esta manera el público objetivo podrá interactuar con la platadorma de forma más amigable.

![Imagen de WhatsApp 2024-09-02 a las 03 04 10_73d5ff2d](https://github.com/user-attachments/assets/69595d97-26ee-4ba9-bba0-521ca8207b3b)

![Imagen de WhatsApp 2024-09-02 a las 03 04 24_0e2c42c4](https://github.com/user-attachments/assets/2b181a3d-bf84-4a33-ac0a-ca96e31b31ad)

![image](https://github.com/user-attachments/assets/ad2c1308-59bc-487f-9438-11303ad0db75)

Como científicos de datos, hemos diseñado varios métodos de recomendación de películas, con la finalidad de poder determinar cual es el que nos brinda el mejor desempeño y calidad al momento de que el usuario interactúa en la plataforma. Entre los métodos utilizados están los siguientes:

 * Recomendador no personalizado

 * Recomendador Content-based

 * Recomendador Collaborative filtering

## ARQUITECTURA DEL PROYECTO

![image](https://github.com/user-attachments/assets/82c51f87-6ed6-4b0e-8197-cd1bdbb05a88)

### 1. CARGANDO BASE DE DATOS

Las bases de datos, se consiguen de la página MOVIELENS, el cual es un servicio libre que nos permite interactuar con las películas, de acuerdo a su rating, popularidad, etc.

![image](https://github.com/user-attachments/assets/3b4544b1-7f89-478b-9629-f058af46f1e4)

Una vez descargadas estas bases de datos, se prosigue a almacenarlas en varios dataframes:

![image](https://github.com/user-attachments/assets/6c63dc08-ee5a-4230-a04b-6be25678ca1f)

### 2. PREPROCESAMIENTO DE DATOS

En esta fase, se procede a analizar todos los dataframes, evaluando la presencia de valores nulos o duplicados. Asimismo, se procede a modificar y validar los tipos de datos presentes en los diferentes dataframes analizados. Se generan nuevas variables (FEATURE ENGINEERING), que nos ayudarán a discriminar mejor nuestras variables y se realiza merges que nos servirán para crear un dataframe final más consolidado y con más valor.

![image](https://github.com/user-attachments/assets/7de5ef92-820b-4784-87d0-1bb653d0441d)

![image](https://github.com/user-attachments/assets/33f70be9-9966-4df1-a0a1-93e0737e4f51)

### 3. ANÁLISIS EXPLORATORIO DE DATOS (EDA)

Es muy importante analizar los datos de nuestro dataframe, con la finalidad de poder conseguir límites, o eliminar ciertas variables que no aporten valor a nuestro propósito. De esta manera, se desarrollaron muchos insights, los cuales nos ayudaron a determinar el rumbo de nuestro modelo de recomendación. A continuación se muestran los insights más importantes:

![image](https://github.com/user-attachments/assets/a421d9a6-e060-41da-ac6c-778da1338ac1)

![image](https://github.com/user-attachments/assets/14b021fe-5dea-4c59-b02a-f945e1bac67f)

![image](https://github.com/user-attachments/assets/c6004b62-1caa-42ac-9a2e-06f224f646b3)

![image](https://github.com/user-attachments/assets/5d6934de-0ea4-41f1-ac85-e19f5277f7f0)

![image](https://github.com/user-attachments/assets/ada10bbc-f6df-4807-b6c0-506a4a6c54cf)

### 4. RECOMENDADOR DE PELÍCULAS

###   4.1 NO PERSONALIZADO

Para este proceso se desarrollo un recomendador de películas, basado en el promedio bayesiano

![image](https://github.com/user-attachments/assets/9a34c91f-2f7d-4024-b4f5-da4d53a3e454)

Se aplicó la siguiente función con la finalidad de poder conseguir el TOP 10 de películas mejor rankeadas de acuerdo a nuestro criterio bayesiano

![image](https://github.com/user-attachments/assets/e2491222-633b-4eb9-a9ff-658c5efeb02f)

En el Notebook quedó representado de esta manera:

![image](https://github.com/user-attachments/assets/20ce1e75-4b09-484c-851d-1fc8c3cff848)

###   4.2 CONTENT - BASED

Para este tipo de recomendador, basado en contenido, se pueden utilizar muchos métodos que nos evaluen la similitud o agrupación por ciertos criterios de las películas. En esta ocasión, se hace uso del método basado en SIMILITUD DE JACCARD y en SIMILITUD DE COSENO.

###     4.2.1 SIMILITUD DE JACCARD:

Esta métrica de Similitud, analiza dos conjuntos de elementos, en los cuales realiza una comparación entre la intersección y la unión de los elementos.


![image](https://github.com/user-attachments/assets/276de59d-1ac5-4558-94dd-8a9d7eb8f4ac)


Se aplicó la siguiente función con la finalidad de poder conseguir el TOP 10 de películas mejor rankeadas de acuerdo a nuestro criterio de SIMILITUD DE JACCARD

![image](https://github.com/user-attachments/assets/6118635e-57cf-4226-b4c1-79036a5e8347)


En el Notebook quedó representado de esta manera:

![image](https://github.com/user-attachments/assets/f2c0ea52-d52d-49b1-9037-cd3b7861a1b6)


###     4.2.2 SIMILITUD DE COSENO

Esta métrica de Similitud, analiza la similitud existente entre dos vectores en un espacio que posee un producto interior con el que se evalúa el valor del coseno del ángulo comprendido entre ellos. Para este caso, realizamos el análisis con los géneros de las películas, en los cuales, vectorizamos cada uno de ellos y los comparamos con todos los demás, consiguiendo valores de similitud de coseno para todos los títulos de películas.

* Se procedió a vectorizar nuestra variable en el dataframe, mediante el cual conseguiremos valores de similitud de coseno para todos los títulos existentes.
  
  ![image](https://github.com/user-attachments/assets/b07811c1-1505-48af-8337-4029d5d18c56)

* Como podemos observar, conseguimos una matriz **cosine_sim**, en la cual están todos los valores de similitud de coseno para todas las variables.

Se aplicó la siguiente función con la finalidad de poder conseguir el TOP 10 de películas mejor rankeadas de acuerdo a nuestro criterio de SIMILITUD DE COSENO

![image](https://github.com/user-attachments/assets/e09f3dfc-7f8c-42e3-a274-f632ecff6212)

En el Notebook quedó representado de esta manera:

![image](https://github.com/user-attachments/assets/7aea50c4-2c6e-4a5c-884e-ecafe7cafb27)

### 5. DEPLOYMENT EN STREAMLIT

En esta ocasión, hacemos nuestro deployment en streamlit, para esto utilizamos las bases de datos ya creadas para poder desarrollar nuestro modelo en streamlit. Además se hace uso de la API de TMDB, donde se puede conseguir información de millones de películas.

![image](https://github.com/user-attachments/assets/79e31aae-b9f0-437b-ad29-ba03cffa130c)

![image](https://github.com/user-attachments/assets/1e2f558b-119b-4e4a-a361-d213ea3e0b2c)

Con este API, se pudo conseguir información de las películas, las cuales nos sirvieron para poder mostrarlo en nuestro recomendador de películas en STREAMLIT, y de esta manera nos quedo un diseño más interactivo y llamativo para el público.

Los posters de las imágenes le da un PLUS a nuestro recomendador, el cual es muy informativo y atractivo para el usuario. A continuación, mostramos el diseño final de nuestro recomendador, ya puesto en producción.

* Les comparto el Link en streamlit:
* Versión Final: https://movie-recommender-play2.app/
* ![image](https://github.com/user-attachments/assets/e53884e1-c806-4de9-ac13-16e1fca2a144)
  




























