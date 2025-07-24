import streamlit as st

from screens.Landing_Page import landing_page
from session_state.session_manager import NavigationSession
from auth.signup import signup_page
from auth.login import login_page

st.session_state.setdefault("user_navigation",NavigationSession())

if(st.session_state.user_navigation.pages[st.session_state.user_navigation.page_index] == 0):
    landing_page()
elif(st.session_state.user_navigation.pages[st.session_state.user_navigation.page_index] == 6):
    signup_page()
elif(st.session_state.user_navigation.pages[st.session_state.user_navigation.page_index] == 7):
    login_page()


if(__name__ == "__main__"):
    pass