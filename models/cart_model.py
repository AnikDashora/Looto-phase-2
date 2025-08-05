import pymysql
import streamlit as st
import os 
import sys


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from database.database_connection import SqlConnection

class UserCart:
    def __init__(self):
        self.user_cart = []
        self.user_cart_items = {}
        self.pending_cart_item = None

    def set_user_cart(self, user_id):
        """
        Fetch cart items from database for a specific user and set user_cart and user_cart_items
        
        Args:
            user_id (int): The ID of the user whose cart to fetch
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = "SELECT * FROM cart_items WHERE user_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id,))
                    result = cursor.fetchall()
                    
                    if result:
                        # Set user_cart with list of dictionaries
                        self.user_cart = result
                        
                        # Create user_cart_items in format {"pid": qty, "pid": qty}
                        self.user_cart_items = {}
                        for item in result:
                            product_id = str(item['product_id'])  # Convert to string for consistency
                            quantity = item['quantity']
                            self.user_cart_items[product_id] = quantity
                            
                    else:
                        # User has no items in cart
                        self.user_cart = []
                        self.user_cart_items = {}
            else:
                st.error("Failed to connect to database")
                self.user_cart = []
                self.user_cart_items = {}
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching cart items: {str(e)}")
            self.user_cart = []
            self.user_cart_items = {}
        except Exception as e:
            st.error(f"Unexpected error while fetching cart items: {str(e)}")
            self.user_cart = []
            self.user_cart_items = {}
            
        finally:
            connect.disconnect()

