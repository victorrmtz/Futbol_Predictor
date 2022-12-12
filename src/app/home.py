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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/LaLiga.svg/1384px-LaLiga.svg.png",
        use_column_width=True)

    st.sidebar.header('Stats Competiciones:')

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        # st.write('')
        st.write('Si quieres contribuir: ', githublink)
    st.success("Selecciona una página.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Introduce la sesion", st.session_state["my_input"])
submit = st.button("Okey")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Inicio de sesión con: ", my_input)