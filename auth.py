import pandas as pd
import os

ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def load_users():

    if not os.path.exists("users.csv"):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)

    if os.stat("users.csv").st_size == 0:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)

    df = pd.read_csv("users.csv")

    # ADMIN ADD
    if ADMIN_USER not in df["username"].values:
        df = pd.concat(
            [df, pd.DataFrame([[ADMIN_USER, ADMIN_PASS]], columns=["username", "password"])],
            ignore_index=True
        )
        df.to_csv("users.csv", index=False)

    return df


def register_user(username, password):
    df = load_users()

    if username in df["username"].values:
        return False

    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv("users.csv", index=False)

    return True


def login_user(username, password):
    df = load_users()
    user = df[(df["username"] == username) & (df["password"] == password)]
    return not user.empty
