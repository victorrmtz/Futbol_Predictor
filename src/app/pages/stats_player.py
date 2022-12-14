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
    page_title='Estadísticas de Jugadores',
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

plt.style.use('fivethirtyeight')

githublink = '[GitHub Repo](https://github.com/victorrmtz/Futbol_Predictor)'

players = pd.read_csv('../../data_limpio/players_l.csv')

st.title('Estadísticas de Jugadores')

records = players.filter(['Id','Player']).sort_values(by='Id').to_dict('records')

with st.sidebar:
    st.image(
        "https://4.bp.blogspot.com/-1LVHjepJLjk/WfVdYb2cZYI/AAAAAAAAAD8/YZSEZaYRhlUdS4gPbu5eUgypSFjwRcGnwCLcBGAs/s1600/la-liga.gif",
        use_column_width=True)

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        st.write(
            'La idea detrás de este proyecto fue motivada por mi pasión por el fútbol y la curiosidad por las estadísticas.' +
            ' Este proyecto utiliza Football Data, que proporciona datos y estadísticas de fútbol.')
        st.write('Si quieres contribuir: ', githublink)

    with st.form('Form1'):
        selection = st.selectbox(
            'Select a Player', options=records,
            format_func = lambda records: f'{records["Player"]}'
        )
        player = selection.get('Id')

        submitted = st.form_submit_button('Run')

    st.sidebar.header('Proximamente')
    st.sidebar.write('- Las 5 grandes Ligas')
    st.sidebar.write('- Analisis de más partidos')
    st.sidebar.write('- Resultados de partidos(Act-2005')

if not submitted:

    st.markdown(
        """
        <style>
        u {
            text-decoration: underline;
            text-decoration-color: #fa4d00;
            }
        </style>
        ### Bienvenido a Estadísticas de Jugadores!\n
        ##### Los resultados se obtienen a través del procesamiento de los datos de los últimos 17 años. \
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

        st.image(players[players.Id == player].foto.iloc[0], width=290)


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
        pitch = mls.Pitch(pitch_color='grass', line_color='white', stripe=True, pitch_length=6, pitch_width=3)
        fig, ax = pitch.draw(figsize=(14, 7))
        if 'MF' in p_str['Pos'].iloc[0]:
            sc1 = pitch.scatter(60, 40, ax=ax, c='#117800', s=3500, zorder=10)
        if 'DF' in p_str['Pos'].iloc[0]:
            sc1 = pitch.scatter(90, 40, ax=ax, c='#FF6800', s=3500, zorder=10)
        if 'FW' in p_str['Pos'].iloc[0]:
            sc1 = pitch.scatter(30, 40, ax=ax, c='#0049FF', s=3500, zorder=10)
        if 'GK' in p_str['Pos'].iloc[0]:
            sc1 = pitch.scatter(115, 40, ax=ax, c='#FF0000', s=3500, zorder=10)
        st.pyplot(fig, facecolor='#0E1117', edgecolor='#0E1117')

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