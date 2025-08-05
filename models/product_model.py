import pymysql
import streamlit as st
import os 
import sys
import random


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from database.database_connection import SqlConnection


class Products:
    def __init__(self):
        self.all_products = self.fetch_all_products()
        self.all_categories = self.fetch_all_categories()
        self.show_products = self.set_show_products()
        self.show_categories = self.set_show_categories()
        self.view_current_product_id = None


    def fetch_all_products(self):
        """Fetch all products from database and store in list of dictionaries"""
        connect = SqlConnection()
        products = []  # Initialize local variable
        
        try:
            if connect.connect():
                sql = "SELECT * FROM products"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    
                    if result:
                        products = result
                    else:
                        products = []
                        st.warning("No products found in database")
            else:
                st.error("Failed to connect to database")
                products = []
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching products: {str(e)}")
            products = []
        except Exception as e:
            st.error(f"Unexpected error while fetching products: {str(e)}")
            products = []
            
        finally:
            connect.disconnect()
        
        return products  # Return the data


    def fetch_all_categories(self):
        """Fetch all categories from database and store in list of dictionaries"""
        connect = SqlConnection()
        categories = []  # Initialize local variable
        
        try:
            if connect.connect():
                sql = "SELECT * FROM categories"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    
                    if result:
                        categories = result
                    else:
                        categories = []
                        st.warning("No categories found in database")
            else:
                st.error("Failed to connect to database")
                categories = []
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching categories: {str(e)}")
            categories = []
        except Exception as e:
            st.error(f"Unexpected error while fetching categories: {str(e)}")
            categories = []
            
        finally:
            connect.disconnect()
        
        return categories  # Return the data


    def set_show_products(self):
        """Shuffle all products and extract first 30 for display"""
        show_products = []  # Initialize local variable
        
        try:
            if not self.all_products:
                self.all_products = self.fetch_all_products()
            
            if self.all_products:
                # Create a copy to avoid modifying original list
                shuffled_products = self.all_products.copy()
                random.shuffle(shuffled_products)
                
                # Extract first 30 products
                show_products = shuffled_products[:30]
            else:
                show_products = []
                st.info("No products available to display")
                
        except Exception as e:
            st.error(f"Error while setting show products: {str(e)}")
            show_products = []
        
        return show_products  # Return the data


    def set_show_categories(self):
        """Shuffle all categories and extract first 30 for display"""
        show_categories = []  # Initialize local variable
        
        try:
            if not self.all_categories:
                self.all_categories = self.fetch_all_categories()
            
            if self.all_categories:
                # Create a copy to avoid modifying original list
                shuffled_categories = self.all_categories.copy()
                random.shuffle(shuffled_categories)
                
                # Extract first 10 categories
                show_categories = shuffled_categories[:10]
            else:
                show_categories = []
                st.info("No categories available to display")
                
        except Exception as e:
            st.error(f"Error while setting show categories: {str(e)}")
            show_categories = []
        
        return show_categories  # Return the data


