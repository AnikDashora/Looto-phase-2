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
        padding-top: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Center content vertically and horizontally with flexbox */
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

    /* Header styling */
    h1[data-baseweb="heading"] {
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0.25em;
        color: #1a237e; /* deep blue */
        text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
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
        0% { width: 0% }
        80%, 100% { width: 15em }
    }

    /* Blinking cursor */
    @keyframes blink {
        50% { border-color: transparent }
    }

    /* Button styling override */
    div.stButton > button {
        background-color: #3949ab;
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        padding: 0.6em 2.4em;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 8px rgba(57, 73, 171, 0.4);
        cursor: pointer;
        width:50%;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #303f9f;
        box-shadow: 0 6px 12px rgba(48, 63, 159, 0.6);
        color:white;
    }
    div.stButton > button p {
        font-size:1.3rem;
        color: inherit; /* Make sure <p> inside button inherits button text color */
    }

    div.stButton > button:hover p {
        color: inherit; /* Ensure no color change on hover for <p> */
    }   
    div.stButton > button:active{
        background-color: #1a237e; /* darker blue for pressed effect */
        box-shadow: inset 0 3px 5px rgba(0,0,0,0.3);
        color: white;
        transform: translateY(2px);
    }
    div.stButton > button:focus-visible, 
    div.stButton > button:focus:not(:active){
        color: white;
        background-color: #303f9f;       /* slightly darker background on focus */
        transition: box-shadow 0.3s ease, background-color 0.3s ease;
    }
    </style>
"""

def landing_page():
    st.markdown(landing_page_styles,unsafe_allow_html=True)
    st.header("Welcome to LOOTO")
    tag_line = "Ab nahi loge tho kab....."
    st.subheader(tag_line)
    st.button("Let's start",on_click=st.session_state.user_navigation.to_signup)

