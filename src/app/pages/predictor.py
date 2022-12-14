import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mplsoccer as mls
from PIL import Image

st.set_page_config(
    page_title='Fútbol Predictor',
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

plt.style.use('fivethirtyeight')

st.title("Fútbol Predictor")

df = pd.read_csv('../../predicciones.csv')

with st.sidebar:
    githublink = '[GitHub Repo](https://github.com/victorrmtz/Futbol_Predictor)'

    st.image(
        "https://4.bp.blogspot.com/-1LVHjepJLjk/WfVdYb2cZYI/AAAAAAAAAD8/YZSEZaYRhlUdS4gPbu5eUgypSFjwRcGnwCLcBGAs/s1600/la-liga.gif",
        use_column_width=True)

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        st.write(
            'La idea detrás de este proyecto fue motivada por mi pasión por el fútbol y la curiosidad por las estadísticas.' +
            ' Este proyecto utiliza Football Data, que proporciona datos y estadísticas de fútbol.')
        st.write('Si quieres contribuir: ', githublink)

    st.sidebar.header('Proximamente')
    st.sidebar.write('- Las 5 grandes Ligas')
    st.sidebar.write('- Analisis de más partidos')
    st.sidebar.write('- Resultados de partidos(Act-2005')

fin = pd.DataFrame()
df['Fecha'] = df[['day', 'month', 'year']].astype(str).apply('-'.join, axis=1)

fin['Fecha'] = df['Fecha']
fin['Local'] = df['HomeTeam']
fin['Visitante'] = df['AwayTeam']

lista = []
cuo = []
for ind,x in enumerate(df.Prediccion):
    if x == 'Home':
        lista.append('Local Gana')
        cuo.append("{0:.2f}".format(df.B365H.iloc[ind]))
    elif x == 'Away':
        lista.append('Visitante Gana')
        cuo.append("{0:.2f}".format(df.B365A.iloc[ind]))
    else:
        lista.append('Empate')
        cuo.append("{0:.2f}".format(df.B365D.iloc[ind]))
fin['Predicción'] = lista
fin['Cuota'] = cuo

fin['Recomendación'] = ['1 DNV', '2 DNV', 'X2', '1 DNV', '1', 'X2', '2 DNV', '1', '2', '1 DNV', 'X2']
fin['Cuota 2'] = ["{0:.2f}".format(1.61),"{0:.2f}".format(1.61),"{0:.2f}".format(1.70),"{0:.2f}".format(1.57),
                  "{0:.2f}".format(1.83),"{0:.2f}".format(1.50),"{0:.2f}".format(1.50),"{0:.2f}".format(2.05),
                  "{0:.2f}".format(2.05),"{0:.2f}".format(1.50),"{0:.2f}".format(1.66)]
fin['Resultado'] = '...'
#fin['Resultado'] = ['🟥','🟥','✅','🟦','✅','✅','✅','🟦','🟥','🟦','✅']
st.table(fin)

footer = """
    <style>
    footer {visibility: hidden;}
    MainMenu {visibility: hidden;}

    # footer:hover,  footer:active {
    #     color: #fa4d00;
    #     background-color: transparent;
    #     text-decoration: underline;
    #     transition: 400ms ease 0s;
    # }
    footer:after {
        content:'Created by Víctor Comendador ©'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    </style>
    """
st.markdown(footer, unsafe_allow_html=True)