import streamlit as st
import pandas as pd
import os

# -----------------------
# ADMIN CREDENTIAL
# -----------------------
ADMIN_USER = "admin"
ADMIN_PASS = "1234"

# -----------------------
# LOAD USERS (CSV)
# -----------------------
def load_users():
    if os.path.exists("users.csv"):
        return pd.read_csv("users.csv")
    else:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)
        return df

# -----------------------
# REGISTER FUNCTION
# -----------------------
def register_user(username, password):
    df = load_users()

    if username in df["username"].values or username == ADMIN_USER:
        return False

    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv("users.csv", index=False)

    return True

# -----------------------
# LOGIN FUNCTION
# -----------------------
def login_user(username, password):

    # ✅ ADMIN LOGIN
    if username == ADMIN_USER and password == ADMIN_PASS:
        return True

    # ✅ CSV LOGIN
    df = load_users()
    user = df[(df["username"] == username) & (df["password"] == password)]

    return not user.empty


# -----------------------
# LOGIN PAGE
# -----------------------
def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

    if st.button("⬅ Back"):
        st.session_state.page = "landing"


# -----------------------
# REGISTER PAGE
# -----------------------
def register_page():
    st.title("📝 Register")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if register_user(username, password):
            st.success("Registered Successfully")
            st.session_state.page = "login"
        else:
            st.error("User already exists or reserved (admin)")

    if st.button("⬅ Back"):
        st.session_state.page = "landing"
