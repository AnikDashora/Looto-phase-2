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

    /* Remove top padding and comfortable horizontal padding */
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

    /* Typography animation element */
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
    }

    /* Typing keyframes */
    @keyframes typing {
        0%   { width: 0% }
        80%,100% { width: 15em }
    }

    /* Blinking cursor */
    @keyframes blink {
        50% { border-color: transparent }
    }

    /* Button styling override */
    div.stButton > button {
        background-color: #3949ab;
        color: white;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.8em 2.4em; /* increased vertical padding for better touch target */
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 8px rgba(57, 73, 171, 0.4);
        cursor: pointer;
        width: 50%;
        max-width: 320px;  /* Limit max width */
        min-width: 160px;  /* Ensure minimum width for tap targets */
        transition: background-color 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
        user-select: none;
    }

    /* Button hover effect */
    div.stButton > button:hover {
        background-color: #303f9f;
        box-shadow: 0 6px 12px rgba(48, 63, 159, 0.6);
        color: white;
    }

    /* Paragraph inside button */
    div.stButton > button p {
        font-size: 1.3rem;
        color: inherit; /* Inherit button text color */
        margin: 0; /* Remove default margin */
        user-select: none;
        pointer-events: none; /* Make text non-interactive */
    }

    /* Paragraph hover inside button */
    div.stButton > button:hover p {
        color: inherit; /* No color change on hover */
    }

    /* Button active (pressed) state */
    div.stButton > button:active {
        background-color: #1a237e; /* darker blue for pressed effect */
        box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.3);
        color: white;
        transform: translateY(2px);
    }

    /* Button focus-visible and focus:not active for accessibility */
    div.stButton > button:focus-visible,
    div.stButton > button:focus:not(:active) {
        color: white;
        background-color: #303f9f;
        outline: 3px solid #1a237e;
        outline-offset: 3px;
        box-shadow: 0 0 8px 3px rgba(26, 35, 126, 0.6);
        transition: box-shadow 0.3s ease, background-color 0.3s ease, outline 0.3s ease;
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
    }

</style>

"""

def landing_page():
    st.markdown(landing_page_styles,unsafe_allow_html=True)
    st.header("Welcome to LOOTO")
    tag_line = "Ab nahi loge tho kab....."
    st.subheader(tag_line)
    st.button("Let's start",on_click=st.session_state.user_navigation.to_signup)

