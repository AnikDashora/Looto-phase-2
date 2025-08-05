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
    
    def handel_signup_login(self):
        if(self.pages[self.page_index - 1] == 0):
            self.to_home_page()
        else:
            self.to_last_page()

    def to_last_page(self):
        if(st.session_state["products"].view_current_product_id is not None and self.pages[self.page_index] == 2):
            st.session_state["products"].view_current_product_id = None
        if(not((self.pages[self.page_index] == 0)
        or
        (self.pages[self.page_index] == 1))):
            self.pages.pop()
            self.page_index -= 1
    
    def to_home_page(self):
        if(self.pages[self.page_index - 1] == 6 or self.pages[self.page_index - 1] == 7):
            self.pages[-1] = 1
        else:
            self.pages.append(1)
            self.page_index += 1 

    def to_product_page(self):
        self.pages.append(2)
        self.page_index += 1

    def to_cart_page(self):
        if(st.session_state["current_user"].user_exist):
            self.pages.append(3)
            self.page_index += 1
        else:
            self.pages.append(3)
            self.pages.append(6)
            self.page_index += 2
    
    def to_order_page(self):
        if(st.session_state["current_user"].user_exist):
            self.pages.append(4)
            self.page_index += 1
        else:
            self.pages.append(4)
            self.pages.append(6)
            self.page_index += 2