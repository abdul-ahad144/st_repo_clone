import streamlit as st
from auth import login_user, register_user

def landing_page():

    # -------- Background --------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #8ea6d1, #d4a5c9);
    }

    header {visibility: hidden;}

    /* Input underline style */
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

    # -------- CENTER USING COLUMNS --------
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("<h2 style='text-align:center;'>User Login</h2>", unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True, index=0)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # LOGIN
        if option == "Login":
            if st.button("LOGIN"):
                if login_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.page = "dashboard"
                    st.session_state.user = username
                    st.rerun()
                else:
                    st.error("Invalid Credentials")

        # REGISTER
        else:
            if st.button("REGISTER"):
                if register_user(username, password):
                    st.success("Registered Successfully")
                else:
                    st.error("User already exists")
