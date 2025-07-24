import mysql.connector
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.database_connection import sql_connection

class UserCart(sql_connection):
    def __init__(self,email):
        self.user_id = None
        self.user_cart = None #this is a dict {pid:qty,}
        self.email = email
        self._user_cart_table = "cart_items"
        self._db_cart = sql_connection()
    
    def set_user_id(self):
        """
            Sets the user_id attribute by querying the database with the user's email.
            
            Raises:
                UserNotFoundError: If no user with the given email is found.
                Exception: For other database related errors.
        """

        sql_query = """
            select user_id from users where email = %s
        """
        sql_data = (self.email,)

        try:
            self._db_cart.cursor.execute(sql_query,sql_data)
            user_record = self._db_cart.cursor.fetchone()
            if(user_record is None):
                self.user_id = None
                raise Exception(f"User with email '{self.email}' does not exist.")
            self.user_id = user_record[0]
        except Exception as e:
            print(f"Error executing query: {e}")

    def set_user_cart(self):
        sql_query = f"""
            select product_id,quantity from {self._user_cart_table}
            where user_id = %s
        """
        sql_data = (self.user_id,)

        try:
            if(self.user_id is None):
                raise Exception(f"User with email '{self.email}' does not exist.")
            self._db_cart.cursor.execute(sql_query,sql_data)
            user_cart_record = self._db_cart.cursor.fetchall() #0 index for pids and 1 for quantity
            self.user_cart = {}
            for pid,qty in user_cart_record:
                self.user_cart[pid] = qty  
        except Exception as e:
            print(f"Error executing query: {e}")

    def add_to_cart(self,product_id):
        if(product_id not in self.user_cart.keys()):
            self.user_cart[product_id] = 1
        else:
            self.user_cart[product_id] += 1
    
    def remove_from_cart(self,product_id):
        if(product_id not in self.user_cart.keys()):
            raise Exception(f"The product with {product_id} doesn't exist")
        
        if(self.user_cart[product_id] == 1):
            del self.user_cart[product_id]
        else:
            self.user_cart[product_id] -= 1
    
    def delete_from_cart(self,product_id):
        if(product_id not in self.user_cart.keys()):
            raise Exception(f"The product with {product_id} doesn't exist")
        else:
            del self.user_cart[product_id]

        