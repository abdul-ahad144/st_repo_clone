import streamlit as st
import pandas as pd
from auth import login_user, register_user, FILE

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
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown('<div class="title">🚀 PragyanAI</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Login / Register</div>', unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True, index=0)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # ------------------------
        # LOGIN
        # ------------------------
        if option == "Login":
            if st.button("Login"):
                if login_user(username, password):

                    # Super-Important: Save login state
                    st.session_state.logged_in = True
                    st.session_state.page = "dashboard"
                    st.session_state.user = username   # 👈 VERY IMPORTANT

                    st.rerun()
                else:
                    st.error("Invalid Credentials")

        # ------------------------
        # REGISTER
        # ------------------------
        else:
            if st.button("Register"):
                if register_user(username, password):
                    st.success("Registered Successfully, now Login")
                else:
                    st.error("User already exists")

        st.markdown('</div>', unsafe_allow_html=True)

    # ------------------------
    # ADMIN PANEL (OUTSIDE CARD)
    # ------------------------
    if st.session_state.get("user") == "admin":

        st.markdown("---")
        st.subheader("📁 Users Data (Admin Only)")

        st.write("File Location:", FILE)

        if st.button("Show Users Data"):
            df = pd.read_csv(FILE)
            st.dataframe(df)

        if st.button("Download users.csv"):
            with open(FILE, "rb") as f:
                st.download_button("Click to Download", f, file_name="users.csv")
