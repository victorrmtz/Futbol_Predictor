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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/LaLiga.svg/1384px-LaLiga.svg.png",
        use_column_width=True)

    st.sidebar.header('Stats Competiciones:')

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        # st.write('')
        st.write('Si quieres contribuir: ', githublink)

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

fin['Recomendación'] = ['1 DNV', '1', 'X2', '2 Handicap +1.0', '1', '1 DNV', 'X2', '1 DNV', 'X2', '1 DNV', '1X']
fin['Cuota 2'] = ["{0:.2f}".format(1.73),"{0:.2f}".format(1.75),"{0:.2f}".format(1.67),"{0:.2f}".format(1.73),
                  "{0:.2f}".format(1.85),"{0:.2f}".format(1.57),"{0:.2f}".format(1.80),"{0:.2f}".format(1.62),
                  "{0:.2f}".format(1.83),"{0:.2f}".format(1.57),"{0:.2f}".format(1.50)]
fin['Resultado'] = ['🟥','🟥','✅','🟦','✅','✅','✅','🟦','🟥','🟦','✅']
st.table(fin)