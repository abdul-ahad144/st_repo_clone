import streamlit as st

def landing_page():
    st.title("🚀 PragyanAI")
    st.subheader("Placement Intelligence Engine")

    st.write("Welcome! Please Login or Register")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login"):
            st.session_state.page = "login"

    with col2:
        if st.button("📝 Register"):
            st.session_state.page = "register"
