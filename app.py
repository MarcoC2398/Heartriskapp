import streamlit as st

st.set_page_config(page_title="Heart Risk App", page_icon="❤️", layout="centered")

st.title("Heart Risk App")
st.write(
    """
    Web_app didattica per stimare una **percentuale di rischio cardiovascolare**
    a partire da alcuni parametri clinici basilari.

    Usa il menu nella **sidebar** per navigare tra le pagine.
    """
)


from ui import render_footer
render_footer("Marco Ciccarelli", "https://www.linkedin.com/in/marcociccarelli", "https://github.com/marcociccarelli")
