import pandas as pd
import os

FILE = "users.csv"

def load_users():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["username", "password", "question", "answer"])
        df.to_csv(FILE, index=False)
    else:
        df = pd.read_csv(FILE)

    return df


def register_user(username, password, question, answer):
    df = load_users()

    if username in df["username"].values:
        return False

    new_user = pd.DataFrame([[username, password, question, answer]],
                            columns=["username", "password", "question", "answer"])

    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(FILE, index=False)
    return True


def login_user(username, password):
    df = load_users()
    user = df[(df["username"] == username) & (df["password"] == password)]
    return not user.empty


def get_security_question(username):
    df = load_users()
    user = df[df["username"] == username]

    if not user.empty:
        return user.iloc[0]["question"]
    return None


def verify_answer(username, answer):
    df = load_users()
    user = df[(df["username"] == username) & (df["answer"] == answer)]
    return not user.empty


def reset_password(username, new_password):
    df = load_users()
    df.loc[df["username"] == username, "password"] = new_password
    df.to_csv(FILE, index=False)
