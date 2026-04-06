import streamlit as st

def landing_page():

    # -----------------------
    # CUSTOM CSS (MODERN UI)
    # -----------------------
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        width: 400px;
        margin: auto;
        margin-top: 100px;
        text-align: center;
    }

    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.2);
        color: white;
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

    # -----------------------
    # CARD UI
    # -----------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("## 🚀 PragyanAI")
    st.markdown("### Login / Register")

    # Toggle
    option = st.radio("Select Option", ["Login", "Register"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # -----------------------
    # LOGIN
    # -----------------------
    if option == "Login":
        if st.button("🔐 Login"):
            if username == "admin" and password == "1234":
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
            st.success("Registered Successfully (Demo)")
            st.info("Use admin / 1234 to login")

    st.markdown('</div>', unsafe_allow_html=True)
