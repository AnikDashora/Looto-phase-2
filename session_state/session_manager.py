import streamlit as st

PAGES = ("looto/screens/landing_page",#0
         "looto/screens/home_page",#1
         "looto/screens/product_page",#2
         "looto/screens/cart_page",#3
         "looto/screens/order_page",#4
         "looto/screens/order_status_page",#5
         "looto/auth/signup_page",#6
         "looto/auth/login_page"#7
        )

class NavigationState:
    """
    A class to manage all navigation-related session states for the Looto application.
    """
    def __init__(self):
        self.pages = [0]
        self.page_index = 0

    def get_current_page(self):
        return self.pages[self.page_index]

    def to_signup_page(self):
        self.pages.append(6)
        self.page_index += 1 
    
    def to_login_page(self):
        self.pages.append(7)
        self.page_index += 1 

    def handel_already_a_user(self):
        self.pages[-1] = 7
    
    def handel_new_user(self):
        self.pages[-1] = 6
    
    def to_last_page(self):
        if(not((self.pages[self.page_index] == 0)
        or
        (self.pages[self.page_index] == 1))):
            self.pages.pop()
            self.page_index -= 1
    
    def to_home_page(self):
        self.pages.append(1)
        self.page_index += 1 

