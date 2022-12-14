import streamlit as st

st.set_page_config(
    page_title='Página Principal',
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

st.title("Página Principal")

with st.sidebar:
    githublink = '[GitHub Repo](https://github.com/victorrmtz/Futbol_Predictor)'

    st.image(
        "https://4.bp.blogspot.com/-1LVHjepJLjk/WfVdYb2cZYI/AAAAAAAAAD8/YZSEZaYRhlUdS4gPbu5eUgypSFjwRcGnwCLcBGAs/s1600/la-liga.gif",
        use_column_width=True)

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        st.write('La idea detrás de este proyecto fue motivada por mi pasión por el fútbol y la curiosidad por las estadísticas.' +
                 ' Este proyecto utiliza Football Data, que proporciona datos y estadísticas de fútbol.')
        st.write('Si quieres contribuir: ', githublink)
    st.success("Selecciona una página.")

    st.sidebar.header('Proximamente')
    st.sidebar.write('- Las 5 grandes Ligas')
    st.sidebar.write('- Analisis de más partidos')
    st.sidebar.write('- Resultados de partidos(Act-2005')

if "victor" not in st.session_state:
    st.session_state["victor"] = ""

my_input = st.text_input("Introduce la sesion", st.session_state["victor"])
submit = st.button("Iniciar")

if submit:
    st.session_state["victor"] = my_input
    st.write("Inicio de sesión con: ", my_input)

    st.markdown(
            """
            <style>
            u {
                text-decoration: underline;
                text-decoration-color: #fa4d00;
                }
            </style>
            ### Bienvenido a Futbol Predictor!\n
            ##### Fútbol Predictor es una aplicación de predicciones de fútbol, calculada a partir de Machine Learning. \
            Los resultados se obtienen a través del procesamiento de los datos de los últimos 17 años. \
            También contamos con un análisis de estadisticas de jugadores y equipos españoles. Os proporcionamos un \
            contenido valioso y único del fútbol español. \n \
            Ligas: La Liga Santander y La Liga SmartBank \n \
            ##### Para empezar, selecciona una página.
            """,
            unsafe_allow_html=True
            )

    col1, col2, col3 = st.columns([.00001, 16, .00001])

    with col1:
        st.write(' ')

    with col2:
        st.image('https://play-lh.googleusercontent.com/IWSnJprqIIAKOrNAhcj6nw9Udjy1rTCfRFJHLColb_cOUaONyHP3P0C1D1lgn271EQ',width=900)

    with col3:
        st.write(' ')

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