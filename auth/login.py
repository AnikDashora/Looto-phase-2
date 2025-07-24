import streamlit as st

remove_header_footer = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
"""

login_page_style = """
<style>
    /* Center the login heading */
    section[data-testid="stMain"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 80vh;
        background: linear-gradient(135deg, #f0f4ff, #d9e4ff);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #222;
        padding: 2rem;
        box-sizing: border-box;
    }
    h2#login {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        font-size: 2.8rem;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        color: #1a237e;
        text-shadow: 1px 1px 3px rgba(26, 35, 126, 0.3);
        letter-spacing: normal;
        line-height: 1.2;
    }

    /* Secondary button (Login) style */
    button[kind="secondary"] {
        display: flex !important;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        background-color: #3949AB;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.65em 2.5em;
        border-radius: 10px;
        border: none;
        box-shadow: 0 5px 12px rgba(57, 73, 171, 0.45);
        cursor: pointer;
        transition: background-color 0.35s ease, box-shadow 0.35s ease;
        min-width: 140px;
        user-select: none;
        width:100%;
    }

    button[kind="secondary"]:hover {
        background-color: #303f9f;
        color:white;
        box-shadow: 0 7px 14px rgba(48, 63, 159, 0.55);
    }

    button[kind="secondary"]:active {
        background-color: #1a237e;
        box-shadow: inset 0 3px 6px rgba(0, 0, 0, 0.35);
        transform: translateY(2px);
    }

    button[kind="secondary"]:focus-visible,
    button[kind="secondary"]:focus:not(:active) {
        outline: 3px solid #1a237e;
        outline-offset: 3px;
        box-shadow: 0 0 8px 3px rgba(26, 35, 126, 0.6);
        background-color: #303f9f;
        color: white;
        transition: box-shadow 0.3s ease, background-color 0.3s ease;
    }

    /* Tertiary button (New User?) style */
    button[kind="tertiary"] {
        background-color: transparent;
        color: #3949AB;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.4em 1em;
        border: none;
        cursor: pointer;
        text-decoration: none;
        user-select: none;
        transition: color 0.25s ease;
        min-width: 120px;
        width:100%;
    }

    button[kind="tertiary"]:hover {
        color: #1a237e;
        text-decoration: underline;
    }

    button[kind="tertiary"]:active {
        color: #121858;
        transform: translateY(1px);
    }

    button[kind="tertiary"]:focus-visible,
    button[kind="tertiary"]:focus:not(:active) {
        outline: none;
        color: #303f9f;
        text-decoration: none;
    }

    button[kind="tertiary"]>div>p{
        font-size:1rem;
        text-align:center;
    }

    /* Center buttons nicely in columns */
    .stColumns > div {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.3rem 0;
        width:100%;
    }

    /* Fade-in animation for form elements */
    h2#login,
    .stElementContainer.st-key-login_user_email,
    .stElementContainer.st-key-login_user_password,
    .stElementContainer.st-key-login_button,
    .stElementContainer.st-key-new_user_button {
        animation: fade_in 1s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        opacity: 0;
        transform: translateY(20px) scale(0.90);
    }

    @keyframes fade_in {
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
            pointer-events: auto;
        }
    }

    /* Input fields styling */
    input[id^="text_input_"] {
        border-radius: 8px;
        border: 1.8px solid #3949AB;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: border-color 0.3s ease;
        box-shadow: none !important;
    }

    input[id^="text_input_"]:focus {
        border-color: #1a237e;
        outline: none;
        box-shadow: 0 0 6px rgba(26, 35, 126, 0.5);
    }

    /* Placeholder text style */
    input[id^="text_input_"]::placeholder {
        color: #7a7a7a;
        font-style: italic;
    }
    .stTextInput > label > div > p {
        font-weight: 700;
        color: black;   /* a blue color */
        font-size: 1rem;
        margin-bottom: 0.25rem;
    }

    /* Error message styling */
    div.stAlert {
        max-width: 350px;
        margin: 0.5rem auto 1rem auto;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
</style>
"""
heading = "<h2 id = 'login'>Login</h2>"
def login_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(login_page_style,unsafe_allow_html=True)
    st.markdown(heading,unsafe_allow_html=True)
    useremail = st.text_input("Email",placeholder="Your Email",key = "login_user_email")
    # email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="Your Password",type="password",key = "login_user_password")
    empty_col,login_btn_col,new_user_btn = st.columns([1,3,1])
    with empty_col:
        st.empty()
    with login_btn_col:
        login_btn = st.button("Login",type="secondary",key = "login_button")
    with new_user_btn:
        st.button(
            "New User?",
            type="tertiary",
            key = "new_user_button",
            on_click=st.session_state.user_navigation.to_signup
        )
    # if(login_btn):
    #     if(email_flag and useremail and if_user_exsits(useremail)):
    #         if(userpassword):
    #             if(verify_user(useremail,userpassword)):
    #                 save_user_state(useremail)
    #                 save_user_cart_item_state(read_user_cart(st.session_state["user_id"]))
    #                 save_user_orders_state(read_user_order(st.session_state["user_id"]))
    #                 user_exist()
    #                 if(st.session_state["pending_cart_item"] is not None):
    #                     add_to_cart(
    #                         st.session_state["user_id"],
    #                         st.session_state["pending_cart_item"],
    #                         st.session_state["user_cart_item"]
    #                     )
    #                     st.session_state["pending_cart_item"] = None
    #                 go_to_last_page()
    #                 st.rerun()
    #             else:
    #                 st.error("Invalid Username or Password")
    #         else:
    #             st.error("Invalid Entries")
    #     else:
    #         st.error("User doesn't Exist")

