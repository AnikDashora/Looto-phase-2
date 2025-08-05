import streamlit as st
import os 
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from session_state.session_manager import NavigationState
from models.user_model import User
from screens.Landing_Page import landing_page
from auth.signup import signup_page
from auth.login import signin_page
from screens.Home import home_page
from screens.Product import product_page
from screens.Cart import cart_page
from screens.Orders import order_page

if("navigation" not in st.session_state):
    st.session_state["navigation"] = NavigationState()
if("current_user" not in st.session_state):
    st.session_state["current_user"] = User()

if(st.session_state["navigation"].get_current_page() == 0):
    landing_page()
elif(st.session_state["navigation"].get_current_page() == 6):
    signup_page()
elif(st.session_state["navigation"].get_current_page() == 7):
    signin_page()
elif (st.session_state["navigation"].get_current_page() == 1):
    home_page()
elif (st.session_state["navigation"].get_current_page() == 2):
    product_page()
elif (st.session_state["navigation"].get_current_page() == 3):
    cart_page()
elif (st.session_state["navigation"].get_current_page() == 4):
    order_page()


if(__name__ == "__main__"):
    pass