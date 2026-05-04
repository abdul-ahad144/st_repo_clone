import pandas as pd
import os

FILE = "users.csv"

ADMIN_USER = "admin"
ADMIN_PASS = "1234"


def load_users():
    # Super-Important: File create if not exists
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(FILE, index=False)

    df = pd.read_csv(FILE, dtype=str)

    # Clean data
    df["username"] = df["username"].astype(str).str.strip()
    df["password"] = df["password"].astype(str).str.strip()

    # Add admin if missing
    if ADMIN_USER not in df["username"].values:
        new = pd.DataFrame([[ADMIN_USER, ADMIN_PASS]], columns=["username", "password"])
        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(FILE, index=False)

    return df


def register_user(username, password):
    df = load_users()

    username = str(username).strip()
    password = str(password).strip()

    if username in df["username"].values:
        return False

    new = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new], ignore_index=True)

    # Super-Important: Save file
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
