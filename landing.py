import streamlit as st
import pandas as pd
from auth import login_user, register_user, FILE

def landing_page():

    # ---------------- UI DESIGN ----------------
    st.markdown("""
    <style>

    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .card {
        background: white;
        padding: 40px;
        border-radius: 20px;
        width: 380px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }

    .title {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 25px;
    }

    .stTextInput input {
        border-radius: 10px !important;
        padding: 10px;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(135deg, #ff7b00, #ff5100);
        color: white;
        font-weight: bold;
        padding: 10px;
    }

    .stRadio > div {
        justify-content: center;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- MAIN CARD ----------------
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="title">🚀 PragyanAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Login / Register</div>', unsafe_allow_html=True)

    option = st.radio("", ["Login", "Register"], horizontal=True, index=0)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # ---------------- LOGIN ----------------
    if option == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

    # ---------------- REGISTER ----------------
    else:
        if st.button("Register"):
            if register_user(username, password):
                st.success("Registered Successfully, now Login")
            else:
                st.error("User already exists")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ADMIN PANEL ----------------
    if st.session_state.get("user") == "admin":

        st.markdown("---")
        st.subheader("📁 Users Data (Admin Only)")

        st.write("File Location:", FILE)

        if st.button("Show Users Data"):
            df = pd.read_csv(FILE)
            st.dataframe(df)

        if st.button("Download users.csv"):
            with open(FILE, "rb") as f:
                st.download_button("Download File", f, file_name="users.csv")
