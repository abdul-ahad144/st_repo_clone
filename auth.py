import pandas as pd

ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def load_users():
    file_path = "users.csv"

    try:
        df = pd.read_csv(file_path)

        if "username" not in df.columns or "password" not in df.columns:
            raise Exception("Invalid structure")

    except:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(file_path, index=False)

    # Super-Important: Ensure admin exists
    if ADMIN_USER not in df["username"].values:
        admin_row = pd.DataFrame(
            [[ADMIN_USER, ADMIN_PASS]],
            columns=["username", "password"]
        )
        df = pd.concat([df, admin_row], ignore_index=True)
        df.to_csv(file_path, index=False)

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
