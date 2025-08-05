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
