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

class NavigationSession:
    def __init__(self):
        self.pages = [0]
        self.page_index = 0
    
    def to_signup(self):
        if(self.pages[-1] == 7):
            self.pages[-1] = 6
        else:
            self.pages.append(6)
            self.page_index += 1
    
    def to_login(self):
        if(self.pages[-1] == 6):
            self.pages[-1] = 7
        else:
            self.pages.append(7)
            self.page_index += 1

    
        
