def load_users():
    import os
    import pandas as pd

    ADMIN_USER = "admin"
    ADMIN_PASS = "1234"

    # File exist nahi karti
    if not os.path.exists("users.csv"):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)

    # File empty hai
    if os.stat("users.csv").st_size == 0:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)

    # Read file
    df = pd.read_csv("users.csv")

    # -----------------------
    # ADMIN ADD (IF NOT PRESENT)
    # -----------------------
    if ADMIN_USER not in df["username"].values:
        admin_row = pd.DataFrame(
            [[ADMIN_USER, ADMIN_PASS]],
            columns=["username", "password"]
        )
        df = pd.concat([df, admin_row], ignore_index=True)
        df.to_csv("users.csv", index=False)

    return df
