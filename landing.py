import streamlit as st
from auth import login_user, register_user, get_security_question, verify_answer, reset_password

def landing_page():

    # -------- UI --------
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #8ea6d1, #d4a5c9);
    }

    header {visibility: hidden;}

    .stTextInput input {
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid #1e293b !important;
        border-radius: 0 !important;
        color: #1e293b !important;
    }

    .stButton button {
        width: 100%;
        background: #0f2a44;
        color: white;
        padding: 12px;
        border-radius: 0;
        font-weight: bold;
    }

    .stRadio > div {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # -------- STATE --------
    if "forgot" not in st.session_state:
        st.session_state.forgot = False

    # -------- CENTER --------
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<h2 style='text-align:center;'>User Login</h2>", unsafe_allow_html=True)

        option = st.radio("", ["Login", "Register"], horizontal=True)

        username = st.text_input("Email ID")
        password = st.text_input("Password", type="password")

        # -------- BUTTONS (PERFECT ALIGN) --------
        colA, colB = st.columns(2)

        with colA:
            login_clicked = st.button("LOGIN")

        with colB:
            forgot_clicked = st.button("Forgot Password?")

        # -------- LOGIN --------
        if option == "Login" and login_clicked:
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid Credentials")

        # -------- REGISTER --------
        if option == "Register":

            question = st.selectbox("Security Question", [
                "Your favourite pet?",
                "Your childhood school?",
                "Your favourite colour?"
            ])

            answer = st.text_input("Answer")

            if st.button("REGISTER"):
                if register_user(username, password, question, answer):
                    st.success("Registered Successfully")
                else:
                    st.error("User already exists")

        # -------- FORGOT CLICK --------
        if forgot_clicked:
            st.session_state.forgot = True

        # -------- RESET FLOW --------
        if st.session_state.forgot:

            st.markdown("---")
            st.subheader("Reset Password")

            fp_username = st.text_input("Enter Username")

            if fp_username:
                question = get_security_question(fp_username)

                if question:
                    st.write(f"Security Question: {question}")

                    answer = st.text_input("Answer")
                    new_pass = st.text_input("New Password", type="password")

                    if st.button("Reset Password"):
                        if verify_answer(fp_username, answer):
                            reset_password(fp_username, new_pass)
                            st.success("Password Reset Successful")
                            st.session_state.forgot = False
                        else:
                            st.error("Wrong Answer")
                else:
                    st.error("User not found")
