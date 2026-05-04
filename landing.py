import streamlit as st
from auth import login_user, register_user

def landing_page():

    st.markdown("""
    <style>

    /* Light Royal Blue Background */
    .stApp {
        background: linear-gradient(135deg, #dbeafe, #eff6ff);
    }

    /* ONLY remove top header safely */
    header {visibility: hidden;}

    /* Center Card */
    .card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 35px;
        max-width: 400px;
        margin: 120px auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }

    /* Title */
    .title {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        color: #1e3a8a;
    }

    .subtitle {
        text-align: center;
        color: #475569;
        margin-bottom: 20px;
    }

    /* Inputs */
    .stTextInput input {
        border-radius: 10px !important;
        padding: 10px;
        border: 1px solid #cbd5f5;
    }

    /* Button */
    .stButton button {
        width: 100%;
        border-radius: 10px;
        background: #3b82f6;
        color: white;
        font-weight: bold;
        padding: 10px;
        border: none;
        transition: 0.3s;
    }

    .stButton button:hover {
        background: #2563eb;
        transform: scale(1.03);
    }

    /* Radio center */
    .stRadio > div {
        justify-content: center;
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

    if option == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

    else:
        if st.button("Register"):
            if register_user(username, password):
                st.success("Registered Successfully")
            else:
                st.error("User already exists")

    st.markdown('</div>', unsafe_allow_html=True)
