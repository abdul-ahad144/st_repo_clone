import streamlit as st

# DEFAULT USERS
if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

    if st.button("⬅ Back"):
        st.session_state.page = "landing"


def register_page():
    st.title("📝 Register")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if username in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[username] = password
            st.success("Registered Successfully")
            st.session_state.page = "login"

    if st.button("⬅ Back"):
        st.session_state.page = "landing"
