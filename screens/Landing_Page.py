import streamlit as st
import time
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)



landing_page_styles = """
    <style>
    /* Hide Streamlit header, menu, and footer */
    #MainMenu, header, footer {
        visibility: hidden !important;
    }

    /* Hide the orange loading progress bar */
    div[data-testid="stDecoration"] {
        display: none !important;
    }

    /* Remove top padding and add comfortable horizontal padding */
    .block-container {
        padding-top: 0 !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Center content vertically and horizontally with flexbox */
    section[data-testid="stMain"] {
        display: flex;
        flex-wrap: wrap;
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

    /* Header styling */
    h1[data-baseweb="heading"] {
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0.25em;
        color: #1a237e; /* deep blue */
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
    }

    /* Subheader styling */
    h2[data-baseweb="heading"] {
        font-size: 1.75rem;
        font-weight: 500;
        margin-bottom: 2rem;
        color: #3949ab; /* medium blue */
    }

    /* Responsive centered headings for login/signup */
    #create-a-account, h2#login {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        font-size: 2.8rem;
        margin: 0.5rem 0 1rem 0;
        color: #1a237e;
        text-shadow: 1px 1px 3px rgba(26, 35, 126, 0.3);
        letter-spacing: normal;
        line-height: 1.2;
    }

    /* Typography animation element - responsive */
    #ab-nahi-loge-tho-kab {
        display: inline-block;
        white-space: nowrap;
        overflow: hidden;
        border-right: 3px solid #3949ab;
        color: #3949ab;
        width: 0;
        animation: typing 3s steps(25, end) 0.75s forwards, blink 0.8s step-end infinite;
        animation-iteration-count: infinite;
        font-weight: 600;
        font-family: 'Courier New', Courier, monospace;
        font-size: 2.25rem; /* base size for desktops */
        max-width: 100%;
        box-sizing: border-box;
    }

    /* Responsive font scaling for animated text */
    @media (max-width: 1200px) {
        #ab-nahi-loge-tho-kab {
            font-size: 2rem;
        }
    }

    @media (max-width: 900px) {
        #ab-nahi-loge-tho-kab {
            font-size: 1.75rem;
        }
    }

    @media (max-width: 600px) {
        #ab-nahi-loge-tho-kab {
            font-size: 1.5rem;
            border-right-width: 2px;
        }
    }

    @media (max-width: 400px) {
        #ab-nahi-loge-tho-kab {
            font-size: 1.25rem;
            border-right-width: 2px;
        }
    }

    /* Typing keyframes */
    @keyframes typing {
        0%   { width: 0; }
        80%,100% { width: 15em; }
    }

    /* Blinking cursor */
    @keyframes blink {
        50% { border-color: transparent; }
    }

    /* Button styling override - primary, secondary button style */
    div.stButton > button {
        background-color: #3949ab;
        color: white;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.8em 2.4em;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 8px rgba(57, 73, 171, 0.4);
        cursor: pointer;
        width: 50%;
        max-width: 320px;
        min-width: 160px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
        user-select: none;
    }

    /* Paragraph inside buttons */
    div.stButton > button p {
        font-size: 1.3rem;
        color: inherit;
        margin: 0;
        user-select: none;
        pointer-events: none;
    }

    /* Hover state */
    div.stButton > button:hover {
        background-color: #303f9f;
        box-shadow: 0 6px 12px rgba(48, 63, 159, 0.6);
        color: white;
    }

    div.stButton > button:hover p {
        color: inherit;
    }

    /* Active (pressed) state */
    div.stButton > button:active {
        background-color: #1a237e;
        box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.3);
        color: white;
        transform: translateY(2px);
    }

    /* Focus-visible and focus:not(:active) states for accessibility */
    div.stButton > button:focus-visible,
    div.stButton > button:focus:not(:active) {
        color: white;
        background-color: #303f9f;
        outline: 3px solid #1a237e;
        outline-offset: 3px;
        box-shadow: 0 0 8px 3px rgba(26, 35, 126, 0.6);
        transition: box-shadow 0.3s ease, background-color 0.3s ease, outline 0.3s ease;
    }

    /* Button style for secondary button (SignUp / Login) */
    button[kind="secondary"] {
        display: flex !important;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        background-color: #3949ab;
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
    }

    button[kind="secondary"]:hover {
        background-color: #303f9f;
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

    /* Button style for tertiary button (Already a user? / New User?) */
    button[kind="tertiary"] {
        background-color: transparent;
        color: #3949ab;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.4em 1em;
        border: none;
        cursor: pointer;
        text-decoration: underline;
        user-select: none;
        transition: color 0.25s ease;
        min-width: 120px;
        display: inline-block;
        margin: 0 auto;
    }

    button[kind="tertiary"]:hover {
        color: #1a237e;
        text-decoration: none;
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

    /* Style paragraph inside tertiary buttons */
    button[kind="tertiary"] > div > p {
        font-size: 1rem;
        font-weight: 600;
        color: #3949ab;
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        user-select: none;
        transition: color 0.25s ease;
    }

    button[kind="tertiary"]:hover > div > p {
        color: #1a237e;
        cursor: pointer;
    }

    button[kind="tertiary"]:active > div > p {
        color: #121858;
    }

    /* Center buttons nicely in columns */
    .stColumns > div {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.3rem 0;
        width: 100%; /* Ensures proper centering */
    }

    /* Fade-in animation for form elements */
    h1#create-a-account,
    h2#login,
    .stElementContainer.st-key-signup_user_name,
    .stElementContainer.st-key-signup_user_email,
    .stElementContainer.st-key-signup_user_password,
    .stElementContainer.st-key-signup_button,
    .stElementContainer.st-key-already_user_button,
    .stElementContainer.st-key-login_user_email,
    .stElementContainer.st-key-login_user_password,
    .stElementContainer.st-key-login_button,
    .stElementContainer.st-key-new_user_button {
        animation: fade_in 1s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        opacity: 0;
        transform: translateY(20px) scale(0.98);
        animation-delay: 0.3s;
    }

    @keyframes fade_in {
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
            pointer-events: auto;
        }
    }

    /* Input fields styling - for inputs with id starting "text_input_" */
    input[id^="text_input_"] {
        width: 100%;
        max-width: 400px;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: 1.8px solid #3949ab;
        font-size: 1rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        box-sizing: border-box;
        box-shadow: none !important;
    }

    input[id^="text_input_"]:focus {
        border-color: #1a237e;
        outline: none;
        box-shadow: 0 0 6px rgba(26, 35, 126, 0.5);
    }

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

    /* Responsive adjustments */

    /* Smaller screens: stack buttons full width and reduce text size */
    @media (max-width: 480px) {
        div.stButton > button {
            width: 100% !important;
            max-width: 100% !important;
            min-width: auto !important;
            font-size: 1.1rem;
            padding: 1em;
        }

        div.stButton > button p {
            font-size: 1.2rem;
        }

        #create-a-account,
        h2#login {
            font-size: 2rem;
        }

        #ab-nahi-loge-tho-kab {
            font-size: 1.25rem;
            border-right-width: 2px;
        }
    }

    /* Medium screens adjustments */
    @media (min-width: 481px) and (max-width: 768px) {
        div.stButton > button {
            width: 65%;
            max-width: 280px;
        }

        div.stButton > button p {
            font-size: 1.3rem;
        }

        #create-a-account,
        h2#login {
            font-size: 2.3rem;
        }

        #ab-nahi-loge-tho-kab {
            font-size: 1.75rem;
        }
    }
</style>


"""

def landing_page():
    st.markdown(landing_page_styles,unsafe_allow_html=True)
    st.header("Welcome to LOOTO")
    tag_line = "Ab nahi loge tho kab....."
    st.subheader(tag_line)
    st.button("Let's start",on_click=st.session_state.user_navigation.to_signup)

