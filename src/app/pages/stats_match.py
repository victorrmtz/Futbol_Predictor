import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import mplsoccer as mls
from PIL import Image
import webbrowser
import urllib.request

st.set_page_config(
    page_title='Eventos de Partido',
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

plt.style.use('fivethirtyeight')

githublink = '[GitHub Repo](https://github.com/victorrmtz/Futbol_Predictor)'

events = pd.read_excel('../../eventos.xlsx', sheet_name='Hoja1')
lineups = pd.read_excel('../../lineups.xlsx', sheet_name='Hoja1')

st.title('Eventos de Partido')

records = events.filter(['team'])[0:2].to_dict('records')

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

    with st.form('Form1'):
        selection_team = st.selectbox(
            'Selecciona un equipo', options=records,
            format_func = lambda records: f'{records["team"]}'
        )
        selection_graf = st.selectbox(
            '¿Qué gráfico deseas ver?',
            ('HeatMap - Pases', 'HeatMap - Tiros', 'HeatMap - Faltas')
        )
        team = selection_team.get('team')
        graf = selection_graf

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
        ### Bienvenido a Eventos de Partido!\n
        ##### Eventos de Partido es una parte de la aplicación en la que analizamos los eventos que ocurren en un partido. \
        Contamos con un análisis estadístico de cada uno de los equipos. Contenido valioso y único del fútbol español. \n \
        Ligas: Madrid Segunda de Aficionados. \n \
        ##### Para empezar, utiliza la columna de la izquierda.
        """,
        unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns([.00001, 16, .00001])

    with col1:
        st.write(' ')

    with col2:
        st.image('https://pbs.twimg.com/media/FilUwJMX0AE8iaN?format=jpg&name=large',width=900)

    with col3:
        st.write(' ')
else:
    e_str = events.loc[(events.team == team)]

    col1, col2 = st.columns([1, 2])

    with col1:
        flamingo_cmap = plt.colors.LinearSegmentedColormap.from_list("Flamingo - 100 colors",
                                                                     ['#e3aca7', '#c03a1d'], N=100)
        el_greco_yellow_cmap_100 = plt.colors.LinearSegmentedColormap.from_list("El Greco Yellow - 100 colors",
                                                                     ['#7c2e2a', '#f2dd44'], N=100)
        # Mapa de calor del equipo
        pitch = mls.VerticalPitch(line_color='#000009', line_zorder=2)
        fig, ax = pitch.draw(figsize=(4.4, 6.4))

        kde = pitch.kdeplot(events[events.team == team].x_location,
                            events[events.team == team].y_location, ax=ax,

                            shade=True, levels=100,

                            shade_lowest=True,
                            cut=4,
                            cmap=el_greco_yellow_cmap_100)
        ax_title = ax.set_title('HeatMap Equipo', fontsize=25, color='#FFFFFF')

        st.pyplot(fig, facecolor='#0E1117', edgecolor='#0E1117')

    with col2:
        pitch = mls.Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
        fig, ax = pitch.draw(figsize=(14, 7), constrained_layout=True, tight_layout=False)
        fig.set_facecolor('#22312b')

        if graf == 'HeatMap - Pases':

            ## Pases Completatos del Retiro
            pitch.arrows(events[(events.team == team) & (events.type == 'Pass') & (
                        events.pass_outcome == 'Complete')].x_location, events[
                             (events.team == team) & (events.type == 'Pass') & (
                                         events.pass_outcome == 'Complete')].y_location,
                         events[(events.team == team) & (events.type == 'Pass') & (
                                     events.pass_outcome == 'Complete')].x_pass_end_location, events[
                             (events.team == team) & (events.type == 'Pass') & (
                                         events.pass_outcome == 'Complete')].y_pass_end_location, width=2,
                         headwidth=5, headlength=7, headaxislength=12, color='#ad993c', ax=ax, label='Pases completados')

            ## Pases Fallados del Retiro
            pitch.arrows(events[(events.team == team) & (events.type == 'Pass') & (
                        events.pass_outcome == 'Incomplete')].x_location, events[
                             (events.team == team) & (events.type == 'Pass') & (
                                         events.pass_outcome == 'Incomplete')].y_location,
                         events[(events.team == team) & (events.type == 'Pass') & (
                                     events.pass_outcome == 'Incomplete')].x_pass_end_location, events[
                             (events.team == team) & (events.type == 'Pass') & (
                                         events.pass_outcome == 'Incomplete')].y_pass_end_location, width=2,
                         headwidth=5, headlength=7, headaxislength=12,
                         color='#ba4f45', ax=ax, label='Pases incompletos')
            ## Leyenda
            ax.legend(facecolor='#22312b', handlelength=2, edgecolor='None', fontsize=15, loc='upper left')

            ## Titulo
            ax_title = ax.set_title('Pases completados vs Pases incompletos', fontsize=25, color='#FFFFFF')
            st.pyplot(fig, facecolor='#0E1117', edgecolor='#0E1117')

        elif graf == 'HeatMap - Tiros':

            ## Goles
            pitch.arrows(events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome == 'Goal')].x_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome == 'Goal')].y_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome == 'Goal')].x_shot_end_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome == 'Goal')].y_shot_end_location,
                         width=2,
                         headwidth=5, headlength=7, headaxislength=12, color='#27FF00', ax=ax, label='Gol')

            ## Pases Fallados del Retiro
            pitch.arrows(events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome != 'Goal')].x_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome != 'Goal')].y_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome != 'Goal')].x_shot_end_location,
                         events[(events.team == team) & (events.type == 'Shot') & (events.shot_outcome != 'Goal')].y_shot_end_location,
                         width=2,
                         headwidth=5, headlength=7, headaxislength=12,
                         color='#ba4f45', ax=ax, label='Tiros Fallidos')
            ## Leyenda
            ax.legend(facecolor='#22312b', handlelength=2, edgecolor='None', fontsize=15, loc='upper left')

            ## Titulo
            ax_title = ax.set_title('Goles vs Tiros Fallidos', fontsize=25, color='#FFFFFF')
            st.pyplot(fig, facecolor='#0E1117', edgecolor='#0E1117')
        elif graf == 'HeatMap - Faltas':

            scatter = pitch.scatter(events[(events.type == 'Foul Committed') & (events.team == team)].x_location,
                events[(events.type == 'Foul Committed') & (events.team == team)].y_location,
                ax=ax, edgecolor='black', facecolor='cornflowerblue', s=250
            )
            ax_title = ax.set_title('Faltas del equipo', fontsize=25, color='#FFFFFF')
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