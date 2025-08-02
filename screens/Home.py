import streamlit as st

remove_header_footer = """
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    /* Hide the orange loading progress bar */
    div[data-testid="stDecoration"] {
        display: none !important;
    }
    .stDeployButton{
        display:none;
    }
    /* Remove top padding to avoid white space */
    .block-container {
        padding-top: 1rem !important;
    }
"""

def home_page():
    st.set_page_config(
        page_title="Looto - Your Trusted Shopping Destination",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )