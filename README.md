# MOVIE RECOMMENDER SYSTEM

Una reconocida plataforma de Streaming, nos proporciona de toda su data sobre las películas en su sistema, con la finalidad de poder crearle un recomendador de películas virtual. De esta manera el público objetivo podrá interactuar con la platadorma de forma más amigable.

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



















