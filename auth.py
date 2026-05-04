import pandas as pd
import os

FILE = "users.csv"

def load_users():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(FILE, index=False)
    else:
        df = pd.read_csv(FILE, dtype=str)

    # -------- CLEAN DATA --------
    df["username"] = df["username"].astype(str).str.strip()
    df["password"] = df["password"].astype(str).str.strip()

    return df


def register_user(username, password):
    df = load_users()

    username = str(username).strip()
    password = str(password).strip()

    if username in df["username"].values:
        return False

    new_user = pd.DataFrame([[username, password]],
                            columns=["username", "password"])

    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(FILE, index=False)
    return True


def login_user(username, password):
    df = load_users()

    username = str(username).strip()
    password = str(password).strip()

    user = df[(df["username"] == username) & (df["password"] == password)]
    return not user.empty
