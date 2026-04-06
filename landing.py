import streamlit as st

def landing_page():
    st.title("Welcome to PragyanAI")

    if st.button("Login"):
        st.session_state.page = "dashboard"
        st.session_state.logged_in = True
