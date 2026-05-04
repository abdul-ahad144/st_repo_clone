import streamlit as st
import pandas as pd
from auth import login_user, register_user, FILE

def landing_page():

    # ---------------- SASSY UI ----------------
    st.markdown("""
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }

    /* Glass Card */
    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 40px;
        max-width: 420px;
        margin: 80px auto;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Title */
    .title {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        color: white;
    }

    .subtitle {
        text-align: center;
        color: #ddd;
        margin-bottom: 25px;
    }

    /* Inputs */
    .stTextInput input {
        background: rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 10px;
        border: none;
    }

    /* Button */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(45deg, #ff512f, #dd2476);
        color: white;
        font-weight: bold;
        padding: 12px;
        border: none;
        transition: 0.3s;
    }

    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #ff512f;
    }

    /* Radio */
    .stRadio > div {
        justify-content: center;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- CARD ----------------
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

    # ---------------- ADMIN PANEL ----------------
    if st.session_state.get("user") == "admin":

        st.markdown("---")
        st.subheader("📁 Users Data (Admin Only)")

        if st.button("Show Users Data"):
            df = pd.read_csv(FILE)
            st.dataframe(df)

        if st.button("Download users.csv"):
            with open(FILE, "rb") as f:
                st.download_button("Download File", f, file_name="users.csv")
