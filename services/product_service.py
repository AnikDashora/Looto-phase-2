import pymysql
import streamlit as st
import os 
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.database_connection import SqlConnection
from models.product_model import Products

class ProductService:
    def set_view_product(product_id, product_obj):
        """
        Set the current product ID to be viewed in the product object
        
        Args:
            product_id: The ID of the product to view
            product_obj: The Products instance to update
        """
        try:
            if product_obj and hasattr(product_obj, 'view_current_product_id'):
                product_obj.view_current_product_id = product_id
                return True
            else:
                print("Invalid product object provided")
                return False
        except Exception as e:
            return False
        
    def fetch_product_details(product_id):
        """
        Fetch product details from database by product ID
        
        Args:
            product_id (int): The ID of the product to fetch
            
        Returns:
            dict: Product details if found, None otherwise
        """
        connect = SqlConnection()
        
        try:
            if connect.connect():
                sql = "SELECT * FROM products WHERE product_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (product_id,))
                    result = cursor.fetchone()
                    
                    if result:
                        return result
                    else:
                        st.warning(f"Product with ID {product_id} not found")
                        return None
            else:
                st.error("Failed to connect to database")
                return None
                
        except pymysql.Error as e:
            st.error(f"Database error while fetching product details: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error while fetching product details: {str(e)}")
            return None
            
        finally:
            connect.disconnect()
        
        return None
    
    @staticmethod
    def filter_according_to_cat(category_id, product_state):
        """
        Filter products according to category and update product_state.show_products
        
        Args:
            category_id (str): Category ID to filter by
            product_state: Products class object containing all_products and show_products
            
        Returns:
            bool: True if successful, False otherwise
        """
        if(not(product_state.filter_categories_id is None or product_state.filter_categories_id != category_id)):
            product_state.show_products = product_state.show_products_copy
            return True
        connect = SqlConnection()
        
        try:
            if not category_id:
                st.error("Category ID is required")
                return False
            
            if not product_state or not hasattr(product_state, 'show_products'):
                st.error("Invalid product state object")
                return False
            
            if connect.connect():
                sql = "SELECT * FROM products WHERE category_id = %s"
                
                with connect.connection.cursor() as cursor:
                    cursor.execute(sql, (category_id,))
                    results = cursor.fetchall()
                    
                    if results:
                        # Update show_products with filtered results
                        product_state.filter_categories_id = category_id
                        product_state.show_products = results
                        return True
                    else:
                        # Set empty list if no products found
                        product_state.show_products = []
                        st.info(f"No products found in category {category_id}")
                        return True  # Still consider as success
            else:
                st.error("Failed to connect to database")
                return False
                
        except pymysql.Error as e:
            st.error(f"Database error while filtering products: {str(e)}")
            return False
        except Exception as e:
            st.error(f"Unexpected error while filtering products: {str(e)}")
            return False
            
        finally:
            connect.disconnect()
        
        return False
