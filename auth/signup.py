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

signup_page_styles = """
<style>
    /* Center the main heading */
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

    #create-a-account {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 1rem;
        color: #1a237e;
        text-shadow: 1px 1px 3px rgba(26, 35, 126, 0.3);
    }
    span{
        display:none;
    }

    /* Sign Up button style */
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
        color:white;
        box-shadow: inset 0 3px 6px rgba(0, 0, 0, 0.35);
        transform: translateY(2px);
    }

    button[kind="secondary"]:focus-visible {
        outline: 3px solid #1a237e; /* prominent outline with deep blue color */
        outline-offset: 3px;
        box-shadow: 0 0 8px 3px rgba(26, 35, 126, 0.6); /* subtle glow */
        background-color: #303f9f; /* slightly darker background on focus */
        color: white;
    }
    button[kind="secondary"]:focus:not(:active) {
        outline: 3px solid #1a237e;   /* prominent deep blue outline */
        outline-offset: 3px;
        box-shadow: 0 0 8px 3px rgba(26, 35, 126, 0.6);  /* subtle glow */
        background-color: #303f9f;    /* slightly darker blue background */
        color: white;
        transition: box-shadow 0.3s ease, background-color 0.3s ease;
    }
    /* Already a user? button style */
    button[kind="tertiary"] {
        background-color: transparent;
        color: #3949AB;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.2em 1em;
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
    }

    /* Fade-in animation for form elements */
    h1#create-a-account,
    .stElementContainer.st-key-signup_user_name,
    .stElementContainer.st-key-signup_user_email,
    .stElementContainer.st-key-signup_user_password,
    .stElementContainer.st-key-signup_button,
    .stElementContainer.st-key-already_user_button {
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
        background-color:white;
    }

    input[id^="text_input_"]:focus {
        border-color: #1a237e;
        outline: none;
        box-shadow: 0 0 6px rgba(26, 35, 126, 0.5);
    }
    .stTextInput > label > div > p {
        font-weight: 700;
        color: black;
        font-size: 1rem;
        margin-bottom: 0.25rem;
    }

    /* Placeholder text style */
    input[id^="text_input_"]::placeholder {
        color: #7a7a7a;
        font-style: italic;
    }

    /* Error message positioning for better visibility */
    div.stAlert {
        max-width: 350px;
        margin: 0.5rem auto 1rem auto;
        font-weight: 600;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
</style>


"""
 
heading = "<h1 id = 'create-a-account'>Create A Account</h1>"

def signup_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(signup_page_styles,unsafe_allow_html=True)
    st.markdown(heading,unsafe_allow_html=True)
    username = st.text_input("Name",placeholder="Jho Doe",key = "signup_user_name")
    # name_flag = validate_name(username)
    useremail = st.text_input("Email",placeholder="Jho.Doe@gmail.com",key = "signup_user_email")
    # email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="!hnfa@2343hgAn",key = "signup_user_password",type="password")
    # password_flag = validate_password(userpassword)
   
    empty_col,signup_btn_col,already_user_btn = st.columns([1,3,1])
    with empty_col:
        st.empty()
    with signup_btn_col:
        signup_btn = st.button("Sign Up",key = "signup_button",type="secondary")
    with already_user_btn:
        st.button(
            "Already a user?",
            key = "already_user_button",
            type = "tertiary",
            on_click=st.session_state.user_navigation.to_login
        )
        
    # if(signup_btn):
    #     if((validate_email and validate_name and validate_password)and(useremail and username and userpassword)):
    #         if(not(if_user_exsits(useremail))):
    #             user_serialization({
    #                 "username":username,
    #                 "useremail":useremail,
    #                 "userpassword":userpassword
    #             })
    #             save_user_state(useremail)
    #             user_exist()
    #             create_user_cart(st.session_state["user_id"])#makes a empty user cart
    #             save_user_cart_item_state(read_user_cart(st.session_state["user_id"]))#saves the list of the cart items
    #             create_user_orders(st.session_state["user_id"])#creates a empty orders in data file
    #             save_user_orders_state(read_user_order(st.session_state["user_id"]))#saves the 
    #             if(st.session_state["pending_cart_item"] is not None):
    #                 add_to_cart(
    #                     st.session_state["user_id"],
    #                     st.session_state["pending_cart_item"],
    #                     st.session_state["user_cart_item"]
    #                 )
    #                 st.session_state["pending_cart_item"] = None
    #             go_to_last_page()
    #             st.rerun()
    #         else:
    #             st.error("User already exist")
    #     else:
    #         st.error("Invalid Entries")