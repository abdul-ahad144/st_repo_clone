import streamlit as st
from auth import login_user, register_user

def landing_page():

    # -----------------------
    # CSS FIXED (CENTER + COLORS)
    # -----------------------
    st.markdown("""
    <style>

    /* Background */
    .main {
        background: linear-gradient(135deg, #eef2f3, #dfe9f3);
    }

    /* Center container */
    .block-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    /* Card */
    .card {
        background: white;
        padding: 40px;
        border-radius: 20px;
        width: 420px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    }

    /* Title */
    .title {
        font-size: 26px;
        font-weight: bold;
        color: #222;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }

    /* Input fields */
    .stTextInput input {
        background-color: #f5f5f5 !important;
        color: black !important;
        border-radius: 10px;
    }

    /* Button */
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
    # CENTER CARD
    # -----------------------
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown('<div class="title">🚀 PragyanAI</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Login / Register</div>', unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # LOGIN
        if option == "Login":
            if st.button("🔐 Login"):
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.page = "dashboard"
                    st.success("Login Successful")
                    st.rerun()
                else:
                    st.error("Invalid Credentials")

        # REGISTER
        else:
            if st.button("📝 Register"):
                if register_user(username, password):
                    st.success("Registered Successfully")
                else:
                    st.error("User already exists")

        st.markdown('</div>', unsafe_allow_html=True)
