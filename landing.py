import streamlit as st
from auth import login_user, register_user

def landing_page():

    # -----------------------
    # PAGE STYLE
    # -----------------------
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }

    .center-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }

    .card {
        background: rgba(255, 255, 255, 0.1);
        padding: 40px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        width: 400px;
        text-align: center;
        box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
    }

    .title {
        font-size: 28px;
        font-weight: bold;
        color: white;
    }

    .subtitle {
        color: #ddd;
        margin-bottom: 20px;
    }

    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.2);
        color: white;
        border-radius: 10px;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        background-color: #ff7b00;
        color: white;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # -----------------------
    # CENTER ALIGNMENT
    # -----------------------
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="title">🚀 PragyanAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Login / Register</div>', unsafe_allow_html=True)

    option = st.radio("", ["Login", "Register"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # -----------------------
    # LOGIN
    # -----------------------
    if option == "Login":
        if st.button("🔐 Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid Credentials")

    # -----------------------
    # REGISTER
    # -----------------------
    else:
        if st.button("📝 Register"):
            if register_user(username, password):
                st.success("Registered Successfully")
            else:
                st.error("User already exists")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
