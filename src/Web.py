import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mplsoccer as mls
from PIL import Image
import webbrowser
import urllib.request

st.set_page_config(
    page_title='Fútbol Predictor',
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

plt.style.use('fivethirtyeight')

githublink = '[GitHub Repo](https://github.com/victorrmtz/Futbol_Predictor)'

players = pd.read_csv('../data_limpio/players_l.csv')

st.title('Fútbol Predictor')

records = players.filter(['Id','Player']).sort_values(by='Id').to_dict('records')

with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/LaLiga.svg/1384px-LaLiga.svg.png",
        use_column_width=True)

    st.sidebar.header('Stats Competiciones:')

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        # st.write('')
        st.write('Si quieres contribuir: ', githublink)

    with st.form('Form1'):
        selection = st.selectbox(
            'Select a Player', options=records,
            format_func = lambda records: f'{records["Player"]}'
        )
        player = selection.get('Id')

        submitted = st.form_submit_button('Run')

if not submitted:

    st.markdown(
        """
        <style>
        u {
            text-decoration: underline;
            text-decoration-color: #fa4d00;
            }
        </style>
        ### Bienvenido a Fútbol Predictor!\n
        ##### Fútbol Predictor es una aplicación de predicciones de fútbol, calculada a partir de Machine Learning. \
        Los resultados se obtienen a través del procesamiento de los datos de los últimos 17 años. \
        También contamos con un análisis de estadisticas de jugadores y equipos españoles. Os proporcionamos un \
        contenido valioso y único del fútbol español. \n \
        Ligas: La Liga Santander y La Liga SmartBank \n \
        ##### Para empezar, utiliza la columna de la izquierda.
        """,
        unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns([.00001, 16, .00001])

    with col1:
        st.write(' ')

    with col2:
        st.image('https://todosobrecamisetas.com/wp-content/uploads/camisetas-la-liga-2020-21.jpg',width=900)

    with col3:
        st.write(' ')

else:
    p_str = players.loc[(players.Id == player)]

    col1, col2, col3, col4, col5 = st.columns([1, 1, 0.33, 0.33, 0.33])

    with col1:
        st.image('https://cdn.sofifa.net/players/notfound_0_60.png', width=290)


    with col2:
        st.text(
            f"Nombre: {p_str['Player'].iloc[0]}"
        )

        st.text(
            f"Equipo: {p_str['Team'].iloc[0]} "
        )
        st.text(
            f"Nacionalidad: {p_str['Nation'].iloc[0]} "
        )
        st.text(
            f"Posicion: {p_str['Pos'].iloc[0]}"
        )
        st.text(
            f"Años: {p_str['Age'].iloc[0]}"
        )
        st.text(
            f"Año nacimiento: {p_str['Born'].iloc[0]}"
        )
        if p_str.Id_Team.iloc[0] < 20:
            st.text(
                "Liga: 1ª División"
            )
        else:
            st.text(
                "Liga: 2ª División"
            )
    with col3:

        st.text('2022-2023')

        st.metric(
            label="Goles",
            value= p_str.Gls.iloc[0]
        )

        st.metric(
            label="Asist",
            value= p_str.Ast.iloc[0]
        )
    with col4:

        st.text(f'{p_str.Pj.iloc[0]}')

        st.metric(
            label="T.Amarillas",
            value= p_str.CrdY.iloc[0]
        )

        st.metric(
            label="T.Rojas",
            value= p_str.CrdR.iloc[0]
        )
    with col5:

        st.text(f'{p_str.Starts.iloc[0]}')

        st.metric(
            label="G/P",
            value= p_str['Gls/Pj'].iloc[0]
        )

        st.metric(
            label="A/P",
            value= p_str['Ast/Pj'].iloc[0]
        )

    col1, col2 = st.columns([1, 2])

    with col2:
        pitch = mls.Pitch(pitch_color='grass', line_color='white', stripe=True, pitch_length=105, pitch_width=68)
        fig, ax = pitch.draw(figsize=(16, 8))
        plt.show()

match = pd.read_csv('../final_match.csv')
stadium = pd.read_csv('../data_limpio/stadiums_l.csv')
teams = pd.read_csv('../data_limpio/teams_l.csv')
