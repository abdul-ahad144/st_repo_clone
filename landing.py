import streamlit as st
from auth import login_user, register_user

def landing_page():

    # -------- UI --------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #8ea6d1, #d4a5c9);
    }

    header {visibility: hidden;}

    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid #1e293b !important;
        border-radius: 0 !important;
        color: #1e293b !important;
    }

    .stButton button {
        width: 100%;
        background: #0f2a44;
        color: white;
        padding: 12px;
        border-radius: 0;
        font-weight: bold;
    }

    .stRadio > div {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------- CENTER --------
    left, center, right = st.columns([1,2,1])

    with center:

        st.markdown("<h2 style='text-align:center;'>User Login</h2>", unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True)

        username = st.text_input("Email ID")
        password = st.text_input("Password", type="password")

        # -------- LOGIN BUTTON --------
        login_clicked = st.button("LOGIN", use_container_width=True)

        # -------- LOGIN LOGIC --------
        if option == "Login" and login_clicked:
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

        # -------- REGISTER --------
        if option == "Register":

            question = st.selectbox("Security Question", [
                "Your favourite pet?",
                "Your childhood school?",
                "Your favourite colour?"
            ])

            answer = st.text_input("Answer")

            register_clicked = st.button("REGISTER", use_container_width=True)

            if register_clicked:
                if register_user(username, password, question, answer):
                    st.success("Registered Successfully")
                else:
                    st.error("User already exists")
