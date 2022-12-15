# Futbol_Predictor

## 🎯 OBJETIVOS

- Obtener datos con diferentes metodos e informaciones (Scraping, CSV, Bases de Datos, APIs, ...).
- Cargar y limpiar los datos extraidos de diferentes webs.
- Crear una base de datos con los datos limpios.
- BBDD de SQL con relaciones lógicas.
- Comprobamos funcionamiento de la Base de Datos con algunas querys.
- Analizamos algunos datos con gráficos e introducirlos a la app.
- Crear modelo de Machine Learning.
- Analizar Jugadores y Partidos.

## 🚶 PASOS A SEGUIR

1. Extraemos los datos de diferentes webs, utilizando Scraping(selenium, bs4) y CSV(Scraping.ipynb).
2. Leemos los archivos .csv extraidos en nuestro Jupyter Notebook(Limpieza.ipynb).
3. Limpiamos los datos con Pandas a partir de DataFrames:
- Eliminamos columna de nulos.
![Nulos](/img/Nulos.jpg)
- Eliminamos columnas con valores que no nos interesan.
- Modificación de valores erróneos en las diferentes columnas (Nombres de equipos, fechas, ints, floats, ...)
4. Una vez limpiamos, los extraemos en un nuevo .csv(data_limpio)
5. Ejecutamos algunas querys(Querys.txt).
6. Analizamos algunos datos por encima, para el futuro(Analisis.ipynb).
7. Creamos variable necesarias de pre-partido para nuestro modelo(Creacion_variables.ipynb)
7. Creamos modelo de Machine Learning(CatBoost) probando diferentes modelos y variables(Predictor.ipynb).
9. Sacamos las predicciones de la Jornada 21(Prediccion_futuro.ipynb).
8. Visualización con StreamLit.

## ℹ️ INFORMACIÓN

- (Stadiums.csv) https://hmong.es/wiki/List_of_stadiums_in_Spain
- (Players.csv & Teams.csv) https://fbref.com/en/comps/12/La-Liga-Stats
- (Matches.csv) https://football-data.co.uk/