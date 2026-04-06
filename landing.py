import streamlit as st

def landing_page():
    st.title("🚀 PragyanAI")
    st.subheader("Placement Intelligence Engine")

    st.write("Click below to enter dashboard")

    if st.button("🔐 Enter Dashboard"):
        st.session_state.logged_in = True
        st.session_state.page = "dashboard"
