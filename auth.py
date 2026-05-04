import pandas as pd
import os
import streamlit as st

# Super-Important: Save in same folder as auth.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "users.csv")

ADMIN_USER = "admin"
ADMIN_PASS = "1234"


def load_users():
    # Show file path on screen
    st.write("📁 Users file location:", FILE)

    # Create file if not exists
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(FILE, index=False)

    df = pd.read_csv(FILE, dtype=str)

    # Clean data
    df["username"] = df["username"].astype(str).str.strip()
    df["password"] = df["password"].astype(str).str.strip()

    # Ensure admin exists
    if ADMIN_USER not in df["username"].values:
        admin_row = pd.DataFrame(
            [[ADMIN_USER, ADMIN_PASS]],
            columns=["username", "password"]
        )
        df = pd.concat([df, admin_row], ignore_index=True)
        df.to_csv(FILE, index=False)

    return df


def register_user(username, password):
    df = load_users()

    username = str(username).strip()
    password = str(password).strip()

    if username in df["username"].values:
        return False

    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)

    df.to_csv(FILE, index=False)

    return True


def login_user(username, password):
    df = load_users()

    username = str(username).strip()
    password = str(password).strip()

    user = df[
        (df["username"] == username) &
        (df["password"] == password)
    ]

    return not user.empty
