import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

PAGES = (
    "looto/screens/landing_page",#0
    "looto/screens/home_page",#1
    "looto/screens/product_page",#2
    "looto/screens/cart_page",#3
    "looto/screens/order_page",#4
    "looto/screens/order_status_page",#5
    "looto/auth/signup_page",#6
    "looto/auth/login_page"#7
)


        
