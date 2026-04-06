import streamlit as st
from landing import landing_page
from dashboard import dashboard

st.set_page_config(page_title="App", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.page == "landing":
    landing_page()

elif st.session_state.page == "dashboard":
    if st.session_state.logged_in:
        dashboard()
    else:
        st.session_state.page = "landing"
