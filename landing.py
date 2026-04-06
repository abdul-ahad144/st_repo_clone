import streamlit as st
from auth import login_user, register_user

def landing_page():

    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #eef2f3, #dfe9f3);
    }

    .card {
        background: white;
        padding: 40px;
        border-radius: 20px;
        width: 400px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    }

    .title {
        font-size: 26px;
        font-weight: bold;
        color: black;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }

    .stTextInput input {
        background-color: #f5f5f5 !important;
        color: black !important;
        border-radius: 10px;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        background-color: #ff7b00;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown('<div class="title">🚀 PragyanAI</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Login / Register</div>', unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if option == "Login":
            if st.button("Login"):
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.page = "dashboard"
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
