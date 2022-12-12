import streamlit as st

st.set_page_config(
    page_title='Página Principal',
    page_icon="👋",
)

st.title("Página Principal")
st.sidebar.success("Selecciona una página.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Introduce la sesion", st.session_state["my_input"])
submit = st.button("Okey")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)