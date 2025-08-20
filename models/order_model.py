import pymysql
import streamlit as st
import os 
import sys


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from database.database_connection import SqlConnection

class Orders:
    def __init__(self):
        self.order_ids = []
    
    def set_order_ids(self, user_id):
        """
        Fetch all order IDs for a specific user from the orders table
        
        Args:
            user_id (str): The user ID to fetch orders for
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = "SELECT order_id FROM orders WHERE user_id = %s order by order_id desc;"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (user_id,))
                    results = cursor.fetchall()
                    if results:
                        # Extract order_ids from the results and store in list
                        self.order_ids = [row['order_id'] for row in results]
                    else:
                        self.order_ids = []
                        st.info(f"No orders found for user {user_id}")
            else:
                st.error("Failed to connect to database")
                self.order_ids = []
                
        except pymysql.Error as e:
            self.order_ids = []
        except Exception as e:
            self.order_ids = []
            
        finally:
            connect.disconnect()
