import streamlit as st
from auth import login_user, register_user

def landing_page():

    st.markdown("""
    <style>

    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #8ea6d1, #d4a5c9);
    }

    header {visibility: hidden;}

    /* Center Layout */
    .center-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 85vh;
    }

    .login-box {
        width: 350px;
        text-align: center;
    }

    .title {
        font-size: 32px;
        font-weight: 300;
        letter-spacing: 2px;
        margin-bottom: 30px;
        color: #1e293b;
    }

    /* Input style (underline look) */
    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid #1e293b !important;
        border-radius: 0 !important;
        color: #1e293b !important;
        padding: 10px;
    }

    .stTextInput input:focus {
        border-bottom: 2px solid #000 !important;
        outline: none;
    }

    /* Button */
    .stButton button {
        width: 100%;
        margin-top: 20px;
        background: #0f2a44;
        color: white;
        border-radius: 0;
        padding: 12px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    /* Radio */
    .stRadio > div {
        justify-content: center;
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)

    # -------- CENTER --------
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown('<div class="title">User Login</div>', unsafe_allow_html=True)

    option = st.radio("", ["Login", "Register"], horizontal=True, index=0)

    username = st.text_input("Email ID")
    password = st.text_input("Password", type="password")

    # -------- LOGIN --------
    if option == "Login":
        if st.button("LOGIN"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

    # -------- REGISTER --------
    else:
        if st.button("REGISTER"):
            if register_user(username, password):
                st.success("Registered Successfully")
            else:
                st.error("User already exists")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
